import app.routers.secret


def test_create_secret(client, create_secret, monkeypatch):
    def fake_create_secret(*args, **kwargs):
        return {"secret_key": f"[{create_secret["secret_key"]}]"}

    monkeypatch.setattr(
        app.routers.secret.secret_utils, "create_one_secret", fake_create_secret
    )

    response = client.post(
        "/generate/",
        json={
            "secret": create_secret["secret"],
            "pass_phrase": create_secret["pass_phrase"],
        },
    )
    assert response.status_code == 200
    assert "secret_key" in response.json()


def test_get_secret(client, create_secret, monkeypatch):
    # потетестить гет-запрос с body параметром походу нельзя,
    # скорее всего pass_phrase придётся в хедер пихать или тип того, а значит переписывать логику
    def fake_get_secret(*args, **kwargs):
        return {"secret": f"[{create_secret["secret"]}]"}

    monkeypatch.setattr(
        app.routers.secret.secret_utils, "get_one_secret", fake_get_secret
    )
    response = client.get(f"/secrets/{create_secret["secret_key"]}")
    assert response.status_code == 200
