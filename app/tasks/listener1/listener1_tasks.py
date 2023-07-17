from typing import Optional
from tasks.celery_app import app as celery_app
from modules.listener1.listener1_service import Listener1Service


@celery_app.task
def listener1_task1(delay: Optional[int] = None) -> object:
    service = Listener1Service()
    response = service.process(delay=delay)
    return response
