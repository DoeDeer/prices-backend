# -*- coding: utf-8 -*-

"""CRUD implementations for customers."""

from app.crud.base import CRUDBase
from app.models import Customer
from app.schemas import customer as schema


class CRUDCustomer(CRUDBase[Customer, schema.CustomerCreate, schema.CustomerUpdate]):
    pass


customer = CRUDCustomer(Customer)
