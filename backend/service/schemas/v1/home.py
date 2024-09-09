from pydantic import AnyHttpUrl, BaseModel


class BackendStatus(BaseModel):
    message: str
    current_version: str
    redoc: AnyHttpUrl
    swagger: AnyHttpUrl


class DBStatus(BaseModel):
    message: str
    adminer: AnyHttpUrl


class HomeResponse(BaseModel):
    backend_status: BackendStatus
    db_status: DBStatus
