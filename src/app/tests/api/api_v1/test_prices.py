# -*- coding: utf-8 -*-

"""V1 api prices endpoints tests."""

from fastapi.testclient import TestClient

from app.core.config import settings


def test_prices_list(client: TestClient, expected_prices) -> None:
    """Test that api returning prices in expected schema and expected way of filtering."""
    response = client.get(f"{settings.API_PREFIX}/prices/?day=2016-01-01&customer=Acme%20Inc.")
    assert response.status_code == 200
    prices = response.json()
    assert len(prices) == len(expected_prices)
    assert prices == expected_prices


def test_read_item(client: TestClient) -> None:
    """Test that api route correctly handles price comparison task."""
    response = client.post(
        f"{settings.API_PREFIX}/prices/compare-price/",
        json={
          "orig_code": "CNSGH",
          "dest_code": "BEZEE",
          "price": 500,
          "day": "2016-01-01",
          "currency": "USD",
        },
    )
    assert response.status_code == 200

    comparison_result = response.json()
    assert comparison_result["average"] == 400
    assert comparison_result["absolute_diff"] == 100
    assert comparison_result["percent_diff"] == 25.0
