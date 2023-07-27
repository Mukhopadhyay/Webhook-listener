from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    REPO_DELAY: int
    REDIS_HOST: str
    REDIS_PORT: int

    FLOWER_HOST: str
    FLOWER_PORT_IN: int
    FLOWER_PORT_OUT: int

    class Config:
        env_file: str = ".env"
        utf_encoding: str = "utf-8"
