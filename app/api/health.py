from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("/health")
async def get_service_health():
    return {"msg": True}
