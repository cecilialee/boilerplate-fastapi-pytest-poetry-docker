import pytest

from fastapi.testclient import TestClient

from app.config import settings
from app.routers.items import fake_items_db


@pytest.fixture
def mock_items_db():
    return fake_items_db


@pytest.fixture
def mock_item_id_exist():
    return "plumbus"


@pytest.fixture
def mock_item_id_not_found():
    return "pickle"


def test_read_items(
    testclient: TestClient, mock_query_token, mock_token_header, mock_items_db
):
    res = testclient.get(
        f"{settings.API_V1_STR}/items",
        params=mock_query_token,
        headers=mock_token_header,
    )
    assert res.status_code == 200
    assert res.json() == mock_items_db


def test_read_items_id_exist(
    testclient: TestClient, mock_query_token, mock_token_header, mock_item_id_exist
):
    res = testclient.get(
        f"{settings.API_V1_STR}/items/{mock_item_id_exist}",
        params=mock_query_token,
        headers=mock_token_header,
    )
    assert res.status_code == 200
    assert res.json() == {"name": "Plumbus", "item_id": "plumbus"}


def test_read_items_id_not_found(
    testclient: TestClient, mock_query_token, mock_token_header, mock_item_id_not_found
):
    res = testclient.get(
        f"{settings.API_V1_STR}/items/{mock_item_id_not_found}",
        params=mock_query_token,
        headers=mock_token_header,
    )
    assert res.status_code == 404
    assert res.json()["detail"] == "Item not found"


def test_update_items_id_exist(
    testclient: TestClient, mock_query_token, mock_token_header, mock_item_id_exist
):
    res = testclient.put(
        f"{settings.API_V1_STR}/items/{mock_item_id_exist}",
        params=mock_query_token,
        headers=mock_token_header,
    )
    assert res.status_code == 200
    assert res.json() == {"item_id": "plumbus", "name": "The great Plumbus"}


def test_update_items_id_not_found(
    testclient: TestClient, mock_query_token, mock_token_header, mock_item_id_not_found
):
    res = testclient.put(
        f"{settings.API_V1_STR}/items/{mock_item_id_not_found}",
        params=mock_query_token,
        headers=mock_token_header,
    )
    assert res.status_code == 403
    assert res.json()["detail"] == "You can only update the item: plumbus"
