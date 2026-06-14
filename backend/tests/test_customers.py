def get_token(client):
    client.post("/auth/register", json={
        "name": "customeruser",
        "email": "customeruser@test.com",
        "password": "customer1234"
    })
    response = client.post("/auth/login", data={
        "username": "customeruser@test.com",
        "password": "customer1234"
    })
    return response.json()["access_token"]


def test_create_customer(client):
    token = get_token(client)
    response = client.post("/customers/",
        json={
            "name": "Test Customer",
            "email": "testcustomer@test.com",
            "contact_no": "03001234567",
            "address": "Lahore, Pakistan"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Customer"


def test_get_customers(client):
    token = get_token(client)
    response = client.get("/customers/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_customer(client):
    token = get_token(client)
    create = client.post("/customers/",
        json={
            "name": "Single Customer",
            "email": "single@test.com",
            "contact_no": "03001234568",
            "address": "Karachi, Pakistan"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    customer_id = create.json()["id"]
    response = client.get(f"/customers/{customer_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == customer_id


def test_update_customer(client):
    token = get_token(client)
    create = client.post("/customers/",
        json={
            "name": "Old Customer",
            "email": "old@test.com",
            "contact_no": "03001234569",
            "address": "Okara, Pakistan"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    customer_id = create.json()["id"]
    response = client.put(f"/customers/{customer_id}",
        json={
            "name": "New Customer Name",
            "address": "Lahore, Pakistan"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Customer Name"


def test_delete_customer(client):
    token = get_token(client)
    create = client.post("/customers/",
        json={
            "name": "Delete Customer",
            "email": "delete@test.com",
            "contact_no": "03001234570",
            "address": "Islamabad, Pakistan"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    customer_id = create.json()["id"]
    response = client.delete(f"/customers/{customer_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    get_response = client.get(f"/customers/{customer_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404


def test_create_customer_without_token(client):
    response = client.post("/customers/",
        json={
            "name": "No Token Customer",
            "email": "notoken@test.com"
        }
    )
    assert response.status_code == 401