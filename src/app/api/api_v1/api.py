# -*- coding: utf-8 -*-

"""Api' v1 router definition."""

from fastapi import APIRouter

from app.api.api_v1.endpoints import prices

api_router = APIRouter()
api_router.include_router(prices.router, prefix="/prices", tags=["prices"])
