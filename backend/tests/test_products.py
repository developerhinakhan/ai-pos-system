def get_token(client):
    client.post("/auth/register", json={
        "name": "productuser",
        "email": "product@test.com",
        "password": "product1234"
    })
    response = client.post("/auth/login", data={
        "username": "product@test.com",
        "password": "product1234"
    })
    return response.json()["access_token"]


def test_create_product(client):
    token = get_token(client)
    response = client.post("/products/",
        json={
            "name": "Test Product",
            "sku": "TEST-001",
            "price": 100.0,
            "stock_quantity": 50,
            "low_stock_alert": 5,
            "category_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    assert response.json()["price"] == 100.0


def test_get_products(client):
    token = get_token(client)
    response = client.get("/products/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_product(client):
    token = get_token(client)
    create = client.post("/products/",
        json={
            "name": "Single Product",
            "sku": "SINGLE-001",
            "price": 200.0,
            "stock_quantity": 10,
            "low_stock_alert": 2,
            "category_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    product_id = create.json()["id"]
    response = client.get(f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == product_id


def test_update_product(client):
    token = get_token(client)
    create = client.post("/products/",
        json={
            "name": "Old Name",
            "sku": "OLD-001",
            "price": 100.0,
            "stock_quantity": 10,
            "low_stock_alert": 2,
            "category_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    product_id = create.json()["id"]
    response = client.put(f"/products/{product_id}",
        json={
            "name": "New Name",
            "price": 200.0
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"
    assert response.json()["price"] == 200.0


def test_delete_product(client):
    token = get_token(client)
    create = client.post("/products/",
        json={
            "name": "Delete Me",
            "sku": "DELETE-001",
            "price": 50.0,
            "stock_quantity": 5,
            "low_stock_alert": 1,
            "category_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    product_id = create.json()["id"]
    response = client.delete(f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    get_response = client.get(f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404


def test_create_product_without_token(client):
    response = client.post("/products/",
        json={
            "name": "No Token",
            "sku": "NO-001",
            "price": 100.0,
            "stock_quantity": 10,
            "low_stock_alert": 2,
            "category_id": 1
        }
    )
    assert response.status_code == 401