# -*- coding: utf-8 -*-

"""Prices v1 api implementation."""

import typing
from datetime import date

from fastapi import APIRouter, Depends

from app.schemas import price as schema
from app import models
from app.api.deps import get_customer_by_title
from app.crud import price as crud
from app import utils

router = APIRouter()


@router.get("/")
async def read_prices(
    customer: models.Customer = Depends(get_customer_by_title),
    day: date = date.today(),
    page: int = 1,
) -> typing.List[schema.Price]:
    """Return delivery prices by provided customer for provided day."""
    result = []
    avg_prices = await utils.get_average_price_for_(day)
    async for pr in crud.iterate_multi(
        with_relations=False,
        where_clause=(models.Price.day == day) & (models.Price.customer == customer.id),
        skip=(page - 1) * 100,
    ):
        result.append(schema.Price(
            orig_code=pr.orig_code,
            dest_code=pr.dest_code,
            price=pr.price,
            day=day,
            **utils.calc_diff_between_(pr.price, avg_prices[f"{pr.orig_code}{pr.dest_code}"]).dict(),
        ))
    return result


@router.post("/compare-price/")
async def compare_price(price: schema.PriceCompareIn) -> schema.PriceCompareOut:
    """Return average metrics price of delivery comparing provided data to other customers."""
    await price.validate_relations()

    price.price = await utils.convert_to_usd(price.currency, price.price)
    avg_prices = await utils.get_average_price_for_(price.day)
    return utils.calc_diff_between_(price.price, avg_prices[f"{price.orig_code}{price.dest_code}"])
