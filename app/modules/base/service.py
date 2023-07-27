from abc import ABCMeta, abstractmethod
from typing import Dict, Any


class BaseService(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass


class BaseProcessService(BaseService, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(
        self,
    ) -> Dict[str, Any]:
        pass
