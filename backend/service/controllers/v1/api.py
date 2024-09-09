from fastapi import APIRouter
from fastapi_pagination import add_pagination

from .post import post

router_v1 = APIRouter()

router_v1.include_router(post.router, tags=["Post"], prefix="/posts")
add_pagination(router_v1)
