# -*- coding: utf-8 -*-

"""Base instances for interacting with database."""

from gino import Gino

db = Gino()


class BaseDBModel(db.Model):
    """Class that contains default fields for every app's database schema."""

    id = db.Column(db.Integer(), primary_key=True)
