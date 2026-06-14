def test_register_success(client):
    response = client.post("/auth/register", json={
        "name": "testuser",
        "email": "test@test.com",
        "password": "test1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_register_duplicate_email(client):
    # Register first time
    client.post("/auth/register", json={
        "name": "testuser2",
        "email": "duplicate@test.com",
        "password": "test1234"
    })
    # Register same email again
    response = client.post("/auth/register", json={
        "name": "testuser3",
        "email": "duplicate@test.com",
        "password": "test1234"
    })
    assert response.status_code == 400

def test_login_success(client):
    # First register
    client.post("/auth/register", json={
        "name": "loginuser",
        "email": "login@test.com",
        "password": "login1234"
    })
    # Then login
    response = client.post("/auth/login", data={
        "username": "login@test.com",
        "password": "login1234"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password(client):
    response = client.post("/auth/login", data={
        "username": "login@test.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401