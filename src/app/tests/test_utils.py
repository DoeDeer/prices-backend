# -*- coding: utf-8 -*-

"""Test that app utils works as expected."""

import datetime

import pytest
from app import utils
from app.db import init_db


@pytest.mark.asyncio
async def test_currency_converting(monkeypatch) -> None:
    """Test that currency converting works as expected."""
    # change endpoint for predictable test
    monkeypatch.setattr(utils, "_OER_MODE_POSTFIX", "historical/2021-12-21.json")

    # USD
    usd = await utils.convert_to_usd("USD", 1000)
    assert usd == 1000

    # EUR
    eur = await utils.convert_to_usd("EUR", 1000)
    assert eur == 1129

    # RUB
    rub = await utils.convert_to_usd("RUB", 1000)
    assert rub == 14

    # NOK
    nok = await utils.convert_to_usd("NOK", 1000)
    assert nok == 112


@pytest.mark.asyncio
async def test_average_price_getting(expected_avg_prices) -> None:
    """Test that average value calcs correctly."""
    await init_db.connect_db()
    try:
        avg_prices = await utils.get_average_price_for_(day=datetime.date(day=1, month=1, year=2016))
        assert len(avg_prices) == 6
        for trip, price in avg_prices.items():
            assert trip in expected_avg_prices
            assert price == expected_avg_prices[trip]
    finally:
        await init_db.disconnect_db()


def test_average_metrics_calcs() -> None:
    """Test that average comparison metrics calcs correctly."""
    avg_price, comparing_price = 600, 300
    metrics = utils.calc_diff_between_(comparing_price, avg_price)

    assert metrics.average == avg_price
    assert metrics.absolute_diff == 300
    assert metrics.percent_diff == 50.0
