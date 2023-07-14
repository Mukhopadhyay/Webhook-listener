import time
from modules.base.service import BaseService


class Listener1Service(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def process(self) -> None:
        time.sleep(3)
