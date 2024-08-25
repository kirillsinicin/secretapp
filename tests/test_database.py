from pymongo.client_session import ClientSession

from app.database import get_session


def test_get_session():
    assert isinstance(next(get_session()), ClientSession)
