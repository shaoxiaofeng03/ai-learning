from fastapi.testclient import TestClient

from week01.app.main import app

client = TestClient(app)


def test_health() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_echo_get() -> None:
    resp = client.get("/echo", params={"text": "你好"})
    assert resp.status_code == 200
    assert resp.json() == {"text": "你好", "length": 2}


def test_echo_post() -> None:
    resp = client.post("/echo", json={"text": "你好"})
    assert resp.status_code == 200
    assert resp.json() == {"text": "你好", "length": 2}


def test_echo_model() -> None:
    resp = client.post("/echo_model", json={"text": "你好", "remark": "备注"})
    assert resp.status_code == 200
    assert resp.json() == {"text": "你好", "length": 2, "remark": "备注"}


def test_echo_rejects_empty() -> None:
    assert client.get("/echo", params={"text": ""}).status_code == 422
    assert client.post("/echo", json={"text": ""}).status_code == 422


def test_index_page() -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Echo 测试页" in resp.text


def test_docs_uses_domestic_cdn() -> None:
    resp = client.get("/docs")
    assert resp.status_code == 200
    assert "cdn.bootcdn.net" in resp.text


def test_add() -> None:
    resp = client.get("/add", params={"a": 1, "b": 2})
    assert resp.status_code == 200
    assert resp.json() == 3


def test_now() -> None:
    resp = client.get("/now")
    assert resp.status_code == 200
    # Check that the response is a valid datetime string
    from datetime import datetime

    try:
        datetime.strptime(resp.json(), "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, "Response is not a valid datetime string"
