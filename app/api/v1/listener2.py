from fastapi import APIRouter

router = APIRouter(prefix="/listener2", tags=["Listener #2"])


@router.post("/")
async def post_data():
    return {"msg": "Listener #2 webhook"}
