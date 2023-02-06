# -*- coding: utf-8 -*-

"""Ports module models implementations."""

from app.db import db


class Port(db.Model):
    """Ports database model."""

    __tablename__ = "ports"

    code = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
