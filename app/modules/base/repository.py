"""
The Base repository class
~~~~~~~~~~~~~~~~~~~~~~~~~
The sole task of this class is to simulate the database CRUD methods
"""
import time
from configs import settings


class BaseRepository:
    def __init__(self) -> None:
        self.connection = None

    def create(self) -> None:
        time.sleep(settings.REPO_DELAY)

    def read(self) -> None:
        time.sleep(settings.REPO_DELAY)

    def update(self) -> None:
        time.sleep(settings.REPO_DELAY)

    def delete(self) -> None:
        time.sleep(settings.REPO_DELAY)
