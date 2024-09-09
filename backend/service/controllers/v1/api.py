from fastapi import APIRouter
from fastapi_pagination import add_pagination

router_v1 = APIRouter()


add_pagination(router_v1)
