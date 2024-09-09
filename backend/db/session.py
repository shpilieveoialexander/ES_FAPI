from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from service.core import settings

# Create engine
engine = create_engine(
    settings.PSQL_DB_URI,
    pool_pre_ping=True,
    echo=False,
)

# Crete session maker
DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
