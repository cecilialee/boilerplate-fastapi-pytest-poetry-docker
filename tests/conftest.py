import pytest

from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def testclient():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def mock_token_header():
    return {"x-token": "fake-super-secret-token"}

@pytest.fixture(scope="module")
def mock_query_token():
    return {"token": "morty"}