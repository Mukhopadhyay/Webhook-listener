"""
Service repository for the health endpoints
"""
import requests
from redis import Redis
from typing import Dict
from configs import settings
from modules.base.service import BaseService


class HealthService(BaseService):
    def __init__(self) -> None:
        super().__init__()
        self.flower_data = None

    def __check_redis(
        self,
    ) -> bool:
        r = Redis(settings.REDIS_HOST, settings.REDIS_PORT, socket_connect_timeout=1)
        return r.ping()

    def __check_flower(
        self,
    ) -> bool:
        try:
            r = requests.get(
                f"http://{settings.FLOWER_HOST}:{settings.FLOWER_PORT_IN}/api/workers",
                timeout=1,
            )
        except Exception as err:
            return False
        else:
            self.flower_data = r.json()
            return r.headers.get("Server", "").find("TornadoServer") != -1

    def __check_workers(self) -> bool:
        return bool(self.flower_data)

    def healthcheck(self) -> Dict[str, bool]:
        redis_health = self.__check_redis()
        flower_health = self.__check_flower()
        worker_health = self.__check_workers()
        return {
            "redis": redis_health,
            "flower": flower_health,
            "celery-worker": worker_health,
            "details": {"flower": self.flower_data},
        }
