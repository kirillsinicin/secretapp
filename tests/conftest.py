import uuid

import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app.database import get_session
from app.utils.secret_utils import encrypt_str_by_cryptocode, hash_str

test_mongo_client = MongoClient("mongodb://kiruha:example@localhost:27018/")


@pytest.fixture
def client():
    from app.main import app

    def get_test_session():
        session = test_mongo_client.start_session()
        try:
            yield session
        finally:
            session.end_session()

    app.dependency_overrides[get_session] = get_test_session

    client = TestClient(app)

    yield client

    test_mongo_client.drop_database(test_mongo_client.secret_db)


@pytest.fixture
def create_secret():
    secret_req_body = {"secret": "qwe", "pass_phrase": "asd"}
    test_secrets_collection = test_mongo_client.secret_db.secrets
    secret_in_db = {
        "secret_key": str(uuid.uuid4()),
        "secret": encrypt_str_by_cryptocode(
            secret_req_body["secret"], secret_req_body["pass_phrase"]
        ),
        "pass_phrase": hash_str(secret_req_body["pass_phrase"]),
    }
    test_secrets_collection.insert_one(secret_in_db)
    return secret_in_db, secret_req_body
