import pytest
from fastapi.testclient import TestClient

from app.database import mongo_client


@pytest.fixture
def client():
    from app.main import app

    test_db = mongo_client.test_db

    client = TestClient(app)

    yield client

    mongo_client.drop_database(test_db)


@pytest.fixture
def create_secret():
    test_secrets_collection = mongo_client.test_db.secrets
    secret_db = {
        "secret_key": "qwe",
        "secret": "asd",
        "pass_phrase": "zxc",
    }
    test_secrets_collection.insert_one(secret_db)
    return {
        "secret_key": secret_db["secret_key"],
        "secret": secret_db["secret"],
        "pass_phrase": secret_db["pass_phrase"],
    }


# @pytest.fixture
# def patch_create_secret(monkeypatch):
#     def fake_create_secret():
#         test_secrets_collection = mongo_client.test_db.secrets
#         secret_db = {
#             "secret_key": "qwe",
#             "secret": "asd",
#             "pass_phrase": "zxc",
#         }
#         test_secrets_collection.insert_one(secret_db)
#         return secret_db["secret_key"]
#
#     monkeypatch.setattr(app.utils.secret_utils, "create_one_secret", fake_create_secret)
