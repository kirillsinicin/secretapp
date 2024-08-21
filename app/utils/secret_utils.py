import uuid

from cryptocode import decrypt, encrypt
from passlib.hash import pbkdf2_sha256
from pymongo.client_session import ClientSession

from app.schemas import CreateSecretReq, CreateSecretRes, GetSecretReq, GetSecretRes


def verify_password(plain_password, hashed_password):
    return pbkdf2_sha256.verify(plain_password, hashed_password)


def hash_str(string: str) -> str:
    return pbkdf2_sha256.hash(string)


def encrypt_str_by_cryptocode(string: str, pass_phrase: str) -> str:
    return encrypt(string, pass_phrase)


def decrypt_str_by_cryptocode(string: str, pass_phrase: str):
    return decrypt(string, pass_phrase)


def hash_secret(secret: CreateSecretReq) -> CreateSecretReq:
    return CreateSecretReq(
        secret=encrypt_str_by_cryptocode(secret.secret, secret.pass_phrase),
        pass_phrase=hash_str(secret.pass_phrase),
    )


def create_one_secret(
    secret: CreateSecretReq, session: ClientSession
) -> CreateSecretRes:
    secret_hash = hash_secret(secret)
    # secret_db = Secret(
    #     secret_key=str(uuid.uuid4()),
    #     secret=secret_hash.secret,
    #     pass_phrase=secret_hash.pass_phrase,
    # )
    secret_db = {
        "secret_key": str(uuid.uuid4()),
        "secret": secret_hash.secret,
        "pass_phrase": secret_hash.pass_phrase,
    }
    secrets_collection = session.client.secret_db.secrets
    with session.start_transaction():
        secrets_collection.insert_one(secret_db)
        return CreateSecretRes(secret_key=secret_db["secret_key"])


def get_one_secret(
    secret_key: str, secret_req: GetSecretReq, session: ClientSession
) -> GetSecretRes | None:
    secrets_collection = session.client.secret_db.secrets
    with session.start_transaction():
        secret_db = secrets_collection.find_one({"secret_key": f"{secret_key}"})
        if secret_db is not None:
            if verify_password(secret_req.pass_phrase, secret_db["pass_phrase"]):
                secrets_collection.delete_one({"secret_key": f"{secret_key}"})
                return GetSecretRes(
                    secret=decrypt_str_by_cryptocode(
                        secret_db["secret"], secret_req.pass_phrase
                    )
                )
        return None
