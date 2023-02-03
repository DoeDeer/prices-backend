# -*- coding: utf-8 -*-

"""Hooks for creating and removing db connection for the app."""

from app.db.base import db
from app.core.config import settings


async def connect_db():
    await db.set_bind(settings.POSTGRES_DSN)


async def disconnect_db():
    await db.pop_bind().close()
