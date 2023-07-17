"""
The Base repository class
~~~~~~~~~~~~~~~~~~~~~~~~~
The sole task of this class is to simulate the database CRUD methods
"""
import time
from typing import Optional, Dict, Any
from configs import settings


class BaseRepository:
    def __init__(self) -> None:
        self.connection = None
        self.DEFAULT_DELAY = settings.REPO_DELAY

    def create(self, delay: Optional[int] = None) -> Dict[str, Any]:
        DELAY = self.DEFAULT_DELAY
        if isinstance(delay, int):
            DELAY = delay

        time.sleep(DELAY)
        return {"message": "SUCESSFUL", "status": 1}

    def read(self, delay: Optional[int] = None) -> Dict[str, Any]:
        DELAY = self.DEFAULT_DELAY
        if isinstance(delay, int):
            DELAY = delay

        time.sleep(DELAY)
        return {"message": "SUCESSFUL", "status": 1}

    def update(self, delay: Optional[int] = None) -> Dict[str, Any]:
        DELAY = self.DEFAULT_DELAY
        if isinstance(delay, int):
            DELAY = delay

        time.sleep(DELAY)
        return {"message": "SUCESSFUL", "status": 1}

    def delete(self, delay: Optional[int] = None) -> Dict[str, Any]:
        DELAY = self.DEFAULT_DELAY
        if isinstance(delay, int):
            DELAY = delay

        time.sleep(DELAY)
        return {"message": "SUCESSFUL", "status": 1}
