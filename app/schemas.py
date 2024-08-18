from pydantic import BaseModel


class CreateSecretReq(BaseModel):
    secret: str
    pass_phrase: str


class CreateSecretRes(BaseModel):
    secret_key: str


class GetSecretReq(BaseModel):
    pass_phrase: str


class GetSecretRes(BaseModel):
    secret: str


class Secret(CreateSecretReq, CreateSecretRes):
    pass
