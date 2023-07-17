from typing import Optional, Dict, Any
from modules.base.service import BaseService
from modules.listener1.listener1_repository import Listener1Repository


class Listener1Service(BaseService):
    def __init__(self) -> None:
        super().__init__()
        self.repository = Listener1Repository()

    def process(self, delay: Optional[int] = None) -> Dict[str, Any]:
        result = self.repository.create(delay=delay)
        print("RESULT:", result)
        return result
