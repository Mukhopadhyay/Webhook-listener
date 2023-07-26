"""
schemas::requests.py
Request schemas for the FastAPI server
"""

from typing import Optional
from configs import settings
from pydantic import BaseModel


class WebhookRequest(BaseModel):
    message: Optional[str] = None
    delay: Optional[int] = settings.REPO_DELAY
