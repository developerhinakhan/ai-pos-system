def get_token(client):
    client.post("/auth/register", json={
        "name": "categoryuser",
        "email": "category@test.com",
        "password": "category1234"
    })
    response = client.post("/auth/login", data={
        "username": "category@test.com",
        "password": "category1234"
    })
    return response.json()["access_token"]


def test_create_category(client):
    token = get_token(client)
    response = client.post("/categories/",
        json={
            "name": "Electronics",
            "description": "Electronic items",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Electronics"


def test_get_categories(client):
    token = get_token(client)
    response = client.get("/categories/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_category(client):
    token = get_token(client)
    create = client.post("/categories/",
        json={
            "name": "Food",
            "description": "Food items",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    category_id = create.json()["id"]
    response = client.get(f"/categories/{category_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == category_id


def test_update_category(client):
    token = get_token(client)
    create = client.post("/categories/",
        json={
            "name": "Old Category",
            "description": "Old description",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    category_id = create.json()["id"]
    response = client.put(f"/categories/{category_id}",
        json={
            "name": "New Category",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Category"


def test_delete_category(client):
    token = get_token(client)
    create = client.post("/categories/",
        json={
            "name": "Delete Me",
            "description": "Will be deleted",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    category_id = create.json()["id"]
    response = client.delete(f"/categories/{category_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    get_response = client.get(f"/categories/{category_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404


def test_create_category_without_token(client):
    response = client.post("/categories/",
        json={
            "name": "No Token",
            "description": "Test",
            "is_active": True
        }
    )
    assert response.status_code == 401