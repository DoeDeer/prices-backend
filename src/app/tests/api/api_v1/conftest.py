# -*- coding: utf-8 -*-

"""For V1 api test fixtures and configurations."""

from typing import List
import pytest


@pytest.fixture
def expected_prices() -> List[dict]:
    """Prices schema and data that should be contained in test database."""
    return [
        {
            "orig_code": "CNSGH",
            "dest_code": "BEANR",
            "price": 300,
            "day": "2016-01-01",
            "average": 400,
            "absolute_diff": 100,
            "percent_diff": 25,
        },
        {
            "orig_code": "CNSGH",
            "dest_code": "BEZEE",
            "price": 300,
            "day": "2016-01-01",
            "average": 400,
            "absolute_diff": 100,
            "percent_diff": 25,
        },
        {
            "orig_code": "CNSGH",
            "dest_code": "DEBRV",
            "price": 500,
            "day": "2016-01-01",
            "average": 600,
            "absolute_diff": 100,
            "percent_diff": 16.7,
        },
        {
            "orig_code": "CNSGH",
            "dest_code": "DEHAM",
            "price": 500,
            "day": "2016-01-01",
            "average": 600,
            "absolute_diff": 100,
            "percent_diff": 16.7,
        },
        {
            "orig_code": "CNSGH",
            "dest_code": "FRLEH",
            "price": 600,
            "day": "2016-01-01",
            "average": 700,
            "absolute_diff": 100,
            "percent_diff": 14.3,
        },
        {
            "orig_code": "CNSGH",
            "dest_code": "NLRTM",
            "price": 700,
            "day": "2016-01-01",
            "average": 800,
            "absolute_diff": 100,
            "percent_diff": 12.5,
        }
    ]
