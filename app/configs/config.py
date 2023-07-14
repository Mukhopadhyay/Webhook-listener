from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    REPO_DELAY: int

    class Config:
        env_file: str = ".env"
        utf_encoding: str = "utf-8"
