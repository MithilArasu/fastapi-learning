from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{user_id}/products")
def get_user_products(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return {"error": "User not found"}

    return user.products