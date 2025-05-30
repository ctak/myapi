# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function is used to get a database session.
# It ensures that the session is closed after use, preventing resource leaks.
# @contextlib.contextmanager # Depnds를 사용하기 때문에 주석 처리
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

