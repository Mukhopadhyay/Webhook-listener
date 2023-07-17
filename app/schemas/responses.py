from pydantic import BaseModel
from typing import Optional, Dict, Any


class CeleryTaskResponse(BaseModel):
    task_id: str
    status: str
    data: Optional[Dict[Any, Any]] = None
    error: Optional[Any] = None
