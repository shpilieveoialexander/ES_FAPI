from sqlalchemy import Column, String, Text

from .base import BaseModel


class Post(BaseModel):
    __tablename__ = "post"
    title = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
