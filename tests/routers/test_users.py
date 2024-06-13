import pytest

from fastapi.testclient import TestClient

from app.config import settings


@pytest.fixture
def mock_username():
    return "jerry"


def test_read_users(testclient: TestClient, mock_query_token):
    res = testclient.get(f"{settings.API_V1_STR}/users", params=mock_query_token)
    assert res.status_code == 200
    assert res.json() == [{"username": "Rick"}, {"username": "Morty"}]

def test_read_user_me(testclient: TestClient, mock_query_token):
    res = testclient.get(f"{settings.API_V1_STR}/users/me", params=mock_query_token)
    assert res.status_code == 200
    assert res.json() == {"username": "fakecurrentuser"}

def test_read_user(testclient: TestClient, mock_query_token, mock_username):
    res = testclient.get(f"{settings.API_V1_STR}/users/{mock_username}", params=mock_query_token)
    assert res.status_code == 200
    assert res.json() == {"username": "jerry"}