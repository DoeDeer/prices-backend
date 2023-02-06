# -*- coding: utf-8 -*-

"""Customers module models implementations."""

from app.db import db, BaseDBModel


class Customer(BaseDBModel):
    """Customer database model."""

    __tablename__ = "customers"

    title = db.Column(db.String(100), nullable=False)
