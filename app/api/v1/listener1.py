from tasks import celery_app
from fastapi import APIRouter
from tasks.celery_app import app
from celery.result import AsyncResult
from schemas.responses import CeleryTaskResponse
from schemas.requests import WebhookRequest


router = APIRouter(prefix="/listener1", tags=["Listener #1"])


def _to_taskout(r: AsyncResult) -> CeleryTaskResponse:
    if r.status == "SUCCESS":
        print("Successful")
        return CeleryTaskResponse(task_id=r.task_id, status=r.status, data=r.result)
    elif r.failed():
        return CeleryTaskResponse(task_id=r.task_id, status=r.status, data=r.traceback)
    else:
        return CeleryTaskResponse(task_id=r.task_id, status=r.status)


@router.post("/", response_model=CeleryTaskResponse)
async def post_data(body: WebhookRequest):
    r: AsyncResult = celery_app.listener1_task1.delay(body.delay)
    return _to_taskout(r)


@router.get("/task/{task_id}", response_model=CeleryTaskResponse)
async def get_status_by_id(task_id: str):
    r = app.AsyncResult(task_id)
    return _to_taskout(r)


@router.delete("/task/{task_id}", response_model=CeleryTaskResponse)
async def delete_task_by_id(task_id: str):
    app.control.revoke(task_id, terminate=True, signal="SIGKILL")
    r = app.AsyncResult(task_id)
    return _to_taskout(r)
