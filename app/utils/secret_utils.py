import uuid
from hashlib import blake2b

from app.database import secrets_collection
from app.schemas import (
    CreateSecretReq,
    CreateSecretRes,
    GetSecretReq,
    GetSecretRes,
    Secret,
)


def hash_str(string: str) -> str:
    return blake2b(string.encode(), digest_size=10).hexdigest()


def hash_secret(secret: CreateSecretReq) -> CreateSecretReq:
    return CreateSecretReq(
        secret=hash_str(secret.secret), pass_phrase=hash_str(secret.pass_phrase)
    )


def create_one_secret(secret: CreateSecretReq) -> CreateSecretRes:
    secret_hash = hash_secret(secret)
    secret_db = Secret(
        secret_key=str(uuid.uuid4()),
        secret=secret_hash.secret,
        pass_phrase=secret_hash.pass_phrase,
    )

    secrets_collection.insert_one(secret_db)
    return CreateSecretRes(secret_key=secret_db.secret_key)


def get_one_secret(secret_key: str, pass_phrase: GetSecretReq) -> GetSecretRes:
    secret_db = secrets_collection.find_one(
        {"secret_key": f"{secret_key}", "pass_phrase": f"{pass_phrase}"}
    )
    return GetSecretRes(secret=secret_db.secret)


# test_secret1 = CreateSecretReq(secret="sisi", pass_phrase="hui")
# test_secret2 = CreateSecretReq(secret="pizda", pass_phrase="hui")
#
# test_secret_db = Secret(secret_key=str(uuid.uuid4()), secret="barebuh", pass_phrase="pidor")
#
# print(hash_secret(test_secret1))
# print(hash_secret(test_secret2))
# print(test_secret_db)
