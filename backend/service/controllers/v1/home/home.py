from typing import Dict

from fastapi import APIRouter, Request

from db.session import DBSession
from service.core import settings
from service.schemas import v1 as schemas_v1

router = APIRouter()


@router.get("/", response_model=schemas_v1.HomeResponse)
async def home(request: Request) -> Dict[str, Dict[str, str]]:
    return {
        "backend_status": {
            "message": "Backend service is working",
            "current_version": f"v{settings.VERSION}",
            "redoc": f"{request.url}redoc",
            "swagger": f"{request.url}docs",
        },
        "db_status": {
            "message": f"DB service {'has' if DBSession else 'has not'} been started",
            "adminer": f"{request.url}adminer",
        },
    }
