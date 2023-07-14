from celery import Celery
from fastapi import APIRouter
from modules.listener1.listener1_service import Listener1Service

router = APIRouter(prefix="/listener1", tags=["Listener #1"])

celery = Celery(
    __name__, broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/0"
)


@router.post("/")
async def post_data():
    service = Listener1Service()
    service.process()
    return {"msg": "Listener #1 webhook"}


@celery.task
def divide(x, y):
    import time

    time.sleep(5)
    return x / y
