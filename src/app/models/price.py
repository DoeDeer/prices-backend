# -*- coding: utf-8 -*-

"""Delivery prices module models implementations."""

from app.db import db, BaseDBModel


class Price(BaseDBModel):
    """Delivery price database model."""

    __tablename__ = "prices"

    orig_code = db.Column(db.String(5), db.ForeignKey('ports.code'), nullable=False)
    dest_code = db.Column(db.String(5), db.ForeignKey('ports.code'), nullable=False)
    customer = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False, index=True)
    day = db.Column(db.Date, nullable=False, index=True)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._orig_port_instance = None
        self._dest_port_instance = None
        self._customer_instance = None

    @property
    def orig_port_instance(self):
        return self._orig_port_instance

    @orig_port_instance.setter
    def orig_port_instance(self, port):
        self._orig_port_instance = port

    @property
    def dest_port_instance(self):
        return self._dest_port_instance

    @dest_port_instance.setter
    def dest_port_instance(self, port):
        self._dest_port_instance = port

    @property
    def customer_instance(self):
        return self._customer_instance

    @customer_instance.setter
    def customer_instance(self, customer):
        self._customer_instance = customer
