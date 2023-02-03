# -*- coding: utf-8 -*-

"""For working with app's configuration tools."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Base class for holding and working with all app configurable parameters."""

    API_VERSION: int = 1

    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    OER_APP_ID: str

    @property
    def API_PREFIX(self) -> str:  # noqa: api param hint
        """Return api prefix."""
        return f"/api/v{self.API_VERSION}"

    @property
    def POSTGRES_DSN(self) -> str:  # noqa: postgres dsn hint
        """Return postgres DSN as link from provided parameters."""
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        case_sensitive = True


settings = Settings()
