from app import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_tickets():
    client = app.test_client()
    response = client.get("/tickets")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["titre"] == "Imprimante en panne"


def test_route_inexistante():
    client = app.test_client()
    response = client.get("/inconnue")
    assert response.status_code == 404


def test_version():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.get_json()