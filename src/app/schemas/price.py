# -*- coding: utf-8 -*-

"""Delivery prices validation schemas implementations."""

import datetime

from pydantic import BaseModel, validator, Field
from fastapi import HTTPException

from app.models import Port, Customer


class PriceBase(BaseModel):
    """Price base validation schema."""

    orig_code: str
    dest_code: str
    price: int = Field(gt=0)

    @validator("dest_code")
    def no_trip(cls, v, values):  # noqa: pydantic things
        """Check that orig and dest codes are not the same."""
        if "orig_code" in values and v == values["orig_code"]:
            raise ValueError("Origin and Destination cant be the same place!")
        return v

    async def validate_relations(self):
        """Validate that db relation fields contains valid values."""
        # validate ports
        ports = await Port.query.where(Port.code.in_([self.orig_code, self.dest_code])).gino.all()
        if len(ports) != 2:
            raise HTTPException(status_code=400, detail="Can't find one or both given ports!")

    class Config:
        orm_mode = True


class PriceCreate(PriceBase):
    """Price creation validation schema."""

    day: datetime.date
    customer: int

    async def validate_relations(self):
        await super().validate_relations()
        # validate customer
        customer = await Customer.get(self.customer)
        if customer is None:
            raise HTTPException(status_code=400, detail="Given user doesn't exists!")


class PriceUpdate(PriceCreate):
    """Price update validation schema."""

    pass


class Price(PriceBase):
    """For users representation data schema."""

    day: datetime.date
    average: int
    absolute_diff: int
    percent_diff: float


class PriceCompareIn(PriceBase):
    """Prices comparing input validation schema."""

    day: datetime.date
    currency: str = "USD"


class PriceCompareOut(BaseModel):
    """Prices comparing output representation data schema."""

    average: int
    absolute_diff: int
    percent_diff: float
