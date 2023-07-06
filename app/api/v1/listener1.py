from fastapi import APIRouter

router = APIRouter(prefix="/listener1", tags=["Listener #1"])


@router.post("/")
async def post_data():
    return {"msg": "Listener #1 webhook"}
