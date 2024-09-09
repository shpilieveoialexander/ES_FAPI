import os
from typing import Any, List, Optional

import ujson
from pydantic import AnyHttpUrl, ConfigDict, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ###########
    # BACKEND #
    ###########
    SERVER_HOST: str = os.getenv("SERVER_HOST")
    BACKEND_HOST: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    BACKEND_PORT: int = os.getenv("BACKEND_PORT", 8000)

    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    VERSION: str = os.getenv("VERSION")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "very_secret_key")

    DEBUG: bool = os.getenv("DEBUG", True)

    DEFAULT_TIME_ZONE: str = os.getenv("DEFAULT_TIME_ZONE", "UTC")

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @field_validator("BACKEND_CORS_ORIGINS")
    def parse_cors_origins(cls, value: str) -> List[str]:
        if isinstance(value, str):
            return ujson.loads(value)
        elif isinstance(value, (list, str)):
            return value

    #############
    # DATABASES #
    #############
    # PSQL
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    PSQL_DB_URI: Optional[str] = None

    @field_validator("PSQL_DB_URI", check_fields=False)
    def build_db_uri(cls, v: Optional[str], info: ConfigDict) -> Any:
        values = info.data
        if isinstance(v, str):
            return v
        return "postgresql+psycopg2://{}:{}@{}:5432/{}".format(
            values.get("POSTGRES_USER"),
            values.get("POSTGRES_PASSWORD"),
            values.get("POSTGRES_SERVER"),
            values.get("POSTGRES_DB"),
        )

    ###########
    # ADMINER #
    ###########
    ADMINER_PORT: int = os.getenv("ADMINER_PORT")

    #################
    # ELASTICSEARCH #
    #################

    ES_HOST: str = os.getenv("ES_HOST")
    ES_PORT: int = os.getenv("ES_PORT")

    class Config:
        case_sensitive = True


settings = Settings()
