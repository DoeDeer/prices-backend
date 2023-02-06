# -*- coding: utf-8 -*-

"""App additional logics implementations."""

import datetime
from collections import defaultdict

from aiohttp import ClientSession
from fastapi import HTTPException
import yarl

from app.core.config import settings
from app.db import db
from app.schemas.price import PriceCompareOut


async def get_average_price_for_(day: datetime.date) -> dict:
    """Return dict with average prices of delivering for given day separated by trip.

    Args:
        day (date): for what day search prices.

    """
    query = db.text(
        "SELECT orig_code, dest_code, SUM(price), COUNT(id) "
        "FROM prices "
        f"WHERE day = '{day.isoformat()}' "
        "GROUP BY orig_code, dest_code"
    )
    results = await db.all(query)
    avg_prices = defaultdict(int)
    for orig, dest, prices_sum, count in results:
        avg_prices[f"{orig}{dest}"] = prices_sum // count if count else 0
    return avg_prices


def calc_diff_between_(price_: int, average: int) -> PriceCompareOut:
    """Calculate differences between given price and average.

    Args:
        price_ (int): price of delivery,
        average (int): average price of delivery for the same day.

    Returns:
        PriceCompareOut: pydantic object with field 'average', 'absolute_diff', 'percent_diff'.
        'average' is the same value as given in args, 'absolute_diff' is ant integer with absolute difference
         between provided average value and price value, 'percent_diff' is percent of difference between previously
         calculated absolute diff and provided average value.

    """
    abs_diff = abs(average - price_)
    return PriceCompareOut(
        average=average,
        absolute_diff=abs_diff,
        percent_diff=round(abs_diff / (average or 1) * 100, 1),
    )


# OER = OpenExchangeRates
_OER_BASE_URL = yarl.URL("https://openexchangerates.org/api/")
_OER_MODE_POSTFIX = "latest.json"


async def convert_to_usd(currency: str, amount: int) -> int:
    """Return given amount converted to USD by today's conversion rate.

    Args:
        currency (str): currency of provided money amount,
        amount (int): amount of money to convert.
    Returns:
        int: converted amount of USD. If currency == 'USD' nothing will happen and amount value would be just returned.

    Raises:
        HTTPException: If there is some troubles with connecting to OpenExchangeRates.
        HTTPException: If provided currency didn't found in OpenExchangeRates catalog.

    """
    if currency == "USD" or amount == 0:
        return amount

    currency = currency.upper()
    async with ClientSession() as s:
        async with s.get(_OER_BASE_URL / _OER_MODE_POSTFIX % {
            "base": "USD",
            "app_id": settings.OER_APP_ID,
        }) as response:
            if response.status != 200:
                raise HTTPException(status_code=500, detail="Sorry, something went wrong, try later.")
            currencies = (await response.json())["rates"]
            if currency not in currencies:
                raise HTTPException(status_code=400, detail="Provided unknown currency.")

            rate = currencies[currency]
            converted = amount / rate
            if int(converted) != converted:
                return int(converted) + 1
            return int(converted)
