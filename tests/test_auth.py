from app import create_app


def test_signup_login_and_logout():
    app = create_app({
        "TESTING": True,
        "SECRET_KEY": "test",
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    client = app.test_client()
    response = client.post("/signup", data={"username": "alice", "password": "secret"})
    assert response.status_code == 302
    assert client.get("/").status_code == 200

    client.post("/logout")
    response = client.post("/login", data={"username": "alice", "password": "wrong"})
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data
    assert client.get("/").status_code == 302

    response = client.post("/login", data={"username": "alice", "password": "secret"})
    assert response.status_code == 302
