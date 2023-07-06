from fastapi import APIRouter
from .listener1 import router as listener1_router
from .listener2 import router as listener2_router

router = APIRouter(prefix="/v1")

router.include_router(listener1_router)
router.include_router(listener2_router)
