from fastapi import FastAPI

from app.routers.secret import secret_router

app = FastAPI()

app.include_router(secret_router)
