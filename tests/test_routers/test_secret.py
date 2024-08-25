def test_create_secret(client, monkeypatch):
    response = client.post(
        "/generate/",
        json={
            "secret": "qwe",
            "pass_phrase": "asd",
        },
    )
    assert response.status_code == 200
    assert "secret_key" in response.json()


def test_get_secret(client, create_secret):
    secret_in_db, secret_req_body = create_secret
    response = client.request(
        method="GET",
        url=f"/secrets/{secret_in_db["secret_key"]}",
        json={
            "pass_phrase": secret_req_body["pass_phrase"],
        },
    )
    assert response.status_code == 200
    assert secret_req_body["secret"] == response.json()["secret"]


def test_get_secret_bad(client, create_secret):
    secret_in_db = create_secret[0]
    response = client.request(
        method="GET",
        url=f"/secrets/{secret_in_db["secret_key"]}",
        json={
            "pass_phrase": "bad_pass_phrase",
        },
    )
    assert response.status_code == 404
