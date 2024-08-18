from typing import Annotated

from fastapi import APIRouter, Body

from app.schemas import CreateSecretReq, CreateSecretRes, GetSecretReq, GetSecretRes
from app.utils.secret_utils import create_one_secret, get_one_secret

secret_router = APIRouter()


@secret_router.post("/generate/")
def create_secret(secret: Annotated[CreateSecretReq, Body()]) -> CreateSecretRes:
    return create_one_secret(secret)


@secret_router.get("/secrets/{secret_key}")
def get_secret(
    secret_key: str, pass_phrase: Annotated[GetSecretReq, Body()]
) -> GetSecretRes:
    # return get_one_secret(secret_key, pass_phrase)  # Реализовать удаление
    # yield get_one_secret(secret_key,pass_phrase)
    pass
