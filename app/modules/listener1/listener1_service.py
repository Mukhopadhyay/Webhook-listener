from typing import Optional, Dict, Any
from modules.base.service import BaseProcessService
from modules.listener1.listener1_repository import Listener1Repository


class Listener1Service(BaseProcessService):
    def __init__(self) -> None:
        super().__init__()
        self.repository = Listener1Repository()

    def process(
        self, delay: Optional[int] = None, message: Optional[str] = None
    ) -> Dict[str, Any]:
        _ = message
        result = self.repository.create(delay=delay)
        print("RESULT:", result)
        return result
