from typing import Annotated

from fastapi import APIRouter, Body, Depends
from pymongo.client_session import ClientSession

from app.database import get_session
from app.schemas import CreateSecretReq, CreateSecretRes, GetSecretReq, GetSecretRes
from app.utils.secret_utils import create_one_secret, get_one_secret

secret_router = APIRouter()


@secret_router.post("/generate/")
def create_secret(
    secret: Annotated[CreateSecretReq, Body()],
    session: ClientSession = Depends(get_session),
) -> CreateSecretRes:
    return create_one_secret(secret, session)


@secret_router.get("/secrets/{secret_key}")
def get_secret(
    secret_key: str,
    pass_phrase: Annotated[GetSecretReq, Body()],
    session: ClientSession = Depends(get_session),
) -> GetSecretRes:
    return get_one_secret(secret_key, pass_phrase, session)
