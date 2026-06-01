from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(255), unique=True)
    password_hash = Column(String)

    products = relationship(
        "Product",
        back_populates="owner"
    )