from fastapi import APIRouter
from celery import Celery

router = APIRouter(prefix="/listener1", tags=["Listener #1"])

celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)


@router.post("/")
async def post_data():
    return {"msg": "Listener #1 webhook"}


@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
