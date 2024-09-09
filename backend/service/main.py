import multiprocessing

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.controllers.v1.api import router_v1
from service.controllers.v1.home import home
from service.core import settings

app = FastAPI(
    title=f"{settings.PROJECT_NAME}",
    version=settings.VERSION,
    openapi_url=f"/openapi.json",
)


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(home.router, tags=["Home"])
app.include_router(router_v1, prefix=f"/api/v1")

# Params
max_workers_count = multiprocessing.cpu_count() * 2 + 1


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.BACKEND_HOST,
        port=settings.BACKEND_PORT,
        log_level="info",
        reload=True,
        workers=max_workers_count,
    )
