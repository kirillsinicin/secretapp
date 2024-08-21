from pymongo import MongoClient

mongo_client = MongoClient("mongodb://kiruha:example@localhost:27017/")


def get_session():
    session = mongo_client.start_session()
    try:
        yield session
    finally:
        session.end_session()
