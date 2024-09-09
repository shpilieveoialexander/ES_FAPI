from sqlalchemy import BigInteger, Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(BigInteger, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=None,
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=False),
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
