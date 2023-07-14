from abc import ABCMeta, abstractmethod


class BaseService(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(
        self,
    ) -> None:
        pass
