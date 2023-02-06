# -*- coding: utf-8 -*-

"""Classical Create, Retrieve, Update, Delete interface implementation package for app's instances."""

from app.crud.customer import customer
from app.crud.price import price

__all__ = ["customer", "price"]
