from fastapi.testclient import TestClient


def test_read_main(testclient: TestClient, mock_query_token):
    res = testclient.get("/", params=mock_query_token)
    assert res.status_code == 200
    assert res.json() == {"message": "Hello World!"}