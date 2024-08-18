from fastapi import FastAPI
from routers.secret import secret_router

app = FastAPI()

app.include_router(secret_router)
