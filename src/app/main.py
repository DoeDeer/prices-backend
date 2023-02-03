# -*- coding: utf-8 -*-

"""App's main instances module."""

import logging
import sys

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db import init_db


def setup_logging(log_level: str = "INFO"):
    """Configure logging output and handlers."""
    std = logging.StreamHandler(stream=sys.stdout)
    std.setLevel(log_level)

    err = logging.StreamHandler(stream=sys.stderr)
    err.setLevel("ERROR")
    logging.basicConfig(
        format="[{asctime}][{levelname}] - {name}: {message}",
        style="{",
        level=log_level,
        handlers=[std, err],
    )


setup_logging()

app = FastAPI(
    title="Prices App", openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)

# On startup routines
app.on_event("startup")(init_db.connect_db)

# On shutdown routines
app.on_event("shutdown")(init_db.disconnect_db)
