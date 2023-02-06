# -*- coding: utf-8 -*-

"""Customers validation schemas implementations."""


from pydantic import BaseModel


class CustomerBase(BaseModel):
    """Customer base validation schema."""
    title: str

    class Config:
        orm_mode = True


class CustomerCreate(CustomerBase):
    """Customer creation validation schema."""

    pass


class CustomerUpdate(CustomerBase):
    """Customer update validation schema."""

    pass


class Customer(CustomerBase):
    """For users representation data schema."""
    id: int
