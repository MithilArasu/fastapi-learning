from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_URL = "postgresql://postgres:Mbalas%40178@localhost:5432/fastapi_learning"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()