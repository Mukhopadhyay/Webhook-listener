from api import utils
from tasks import celery_app
from fastapi import APIRouter
from tasks.celery_app import app
from celery.result import AsyncResult
from schemas.responses import CeleryTaskResponse
from schemas.requests import WebhookRequest
from modules.listener1.listener1_service import Listener1Service


router = APIRouter(prefix="/listener1")


@router.post("/", response_model=CeleryTaskResponse)
async def post_data(body: WebhookRequest):
    r: AsyncResult = celery_app.listener1_task1.delay(body.delay, body.message)
    return utils._to_taskout(r)


@router.get("/task/{task_id}", response_model=CeleryTaskResponse)
async def get_status_by_id(task_id: str):
    r = app.AsyncResult(task_id)
    return utils._to_taskout(r)


@router.delete("/task/{task_id}", response_model=CeleryTaskResponse)
async def delete_task_by_id(task_id: str):
    app.control.revoke(task_id, terminate=True, signal="SIGKILL")
    r = app.AsyncResult(task_id)
    return utils._to_taskout(r)


@router.post("/nonCelery/", deprecated=True)
async def post_data_non_celery(body: WebhookRequest):
    service = Listener1Service()
    result = service.process(body.delay, body.message)
    return result
