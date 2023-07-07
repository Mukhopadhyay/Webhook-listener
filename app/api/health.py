from fastapi import APIRouter, status

router = APIRouter(prefix="/health")


@router.get("/health", status_code=status.HTTP_200_OK)
async def get_service_health():
    """
    Route for the service's health.

    A simple GET request.
    """
    return {"health": 1, "message": "Everything OK! :D"}
