# -*- coding: utf-8 -*-

"""General tests fixtures and configurations."""

from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    """Return http client for working with api routes."""
    with TestClient(app) as c:
        yield c


@pytest.fixture
def expected_avg_prices() -> dict:
    """Return expected avg prices from db on test date."""
    return {
        "CNSGHDEBRV": 600,
        "CNSGHNLRTM": 800,
        "CNSGHDEHAM": 600,
        "CNSGHFRLEH": 700,
        "CNSGHBEANR": 400,
        "CNSGHBEZEE": 400,
    }
