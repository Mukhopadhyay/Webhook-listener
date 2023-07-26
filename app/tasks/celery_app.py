"""
Celery App

This is where we are gonna instantiate the celery application
"""
import os
from celery import Celery
from typing import Optional
from modules.listener1.listener1_service import Listener1Service

R_HOST = os.getenv("REDIS_HOST")
R_PORT = os.getenv("REDIS_PORT")

REDIS_URL = "redis://{}:{}/0".format(R_HOST, R_PORT)


app = Celery(__name__, broker=REDIS_URL, backend=REDIS_URL)


@app.task
def listener1_task1(
    delay: Optional[int] = None, message: Optional[str] = None
) -> object:
    service = Listener1Service()
    response = service.process(delay=delay, message=message)
    return response
