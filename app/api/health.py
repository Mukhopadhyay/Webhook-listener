from fastapi import APIRouter, status
from modules.health.service import HealthService

router = APIRouter(prefix="/health")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_service_health():
    """
    Route for the service's health.

    A simple GET request.
    """
    service = HealthService()
    return service.healthcheck()
