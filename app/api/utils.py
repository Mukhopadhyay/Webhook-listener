from celery.result import AsyncResult
from schemas.responses import CeleryTaskResponse


def _to_taskout(r: AsyncResult) -> CeleryTaskResponse:
    if r.status == "SUCCESS":
        print("Successful")
        return CeleryTaskResponse(task_id=r.task_id, status=r.status, data=r.result)
    elif r.failed():
        return CeleryTaskResponse(task_id=r.task_id, status=r.status, data=r.traceback)
    else:
        return CeleryTaskResponse(task_id=r.task_id, status=r.status)
