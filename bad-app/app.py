import time
from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, FastAPI

router = APIRouter(tags=["Listener #1"])


class RequestBody(BaseModel):
    delay: Optional[int] = 3


class Response(BaseModel):
    status: int = 1
    message: str = "Finished task"


@router.post("/v1/listener1")
def post_data(body: RequestBody):
    time.sleep(body.delay)
    return Response()

