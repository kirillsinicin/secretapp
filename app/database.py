from pymongo import MongoClient

from app.config import settings

mongo_client = MongoClient(str(settings.database_url))


def get_session():
    session = mongo_client.start_session()
    try:
        yield session
    finally:
        session.end_session()
