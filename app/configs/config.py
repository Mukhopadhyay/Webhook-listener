from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PORT: int
    HOST_DOCS: bool

    MODE: str
    WORKERS: int
    LOG_LEVEL: str
    WORKDIR: str

    REPO_DELAY: int

    # Redis settings
    REDIS_HOST: str
    REDIS_PORT: int

    FLOWER_HOST: str
    FLOWER_PORT_IN: int
    FLOWER_PORT_OUT: int

    class Config:
        env_file: str = ".env"
        utf_encoding: str = "utf-8"
