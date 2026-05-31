from fastapi import FastAPI
from models.user import User
from models.product import Product
from routers.product import router as product_router
from routers.user import router as user_router

app = FastAPI()

app.include_router(product_router)
app.include_router(user_router)