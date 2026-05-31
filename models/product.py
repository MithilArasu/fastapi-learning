from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    price = Column(Numeric(10, 2))
    stock = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="products"
    )