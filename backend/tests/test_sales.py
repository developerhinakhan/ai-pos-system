def get_token(client):
    client.post("/auth/register", json={
        "name": "salesuser",
        "email": "sales@test.com",
        "password": "sales1234"
    })
    response = client.post("/auth/login", data={
        "username": "sales@test.com",
        "password": "sales1234"
    })
    return response.json()["access_token"]


def create_category(client, token, name="Sale Category"):
    response = client.post("/categories/",
        json={
            "name": name,
            "description": "Test",
            "is_active": True
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()["id"]


def create_product(client, token, category_id, sku="SALE-001"):
    response = client.post("/products/",
        json={
            "name": "Sale Product",
            "sku": sku,
            "price": 100.0,
            "stock_quantity": 50,
            "low_stock_alert": 5,
            "category_id": category_id
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()["id"]


def test_create_sale(client):
    token = get_token(client)
    category_id = create_category(client, token, "Category One")
    product_id = create_product(client, token, category_id, "SALE-001")
    response = client.post("/sales/",
        json={
            "payment_method": "cash",
            "discount": 0,
            "tax": 0,
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2,
                    "unit_price": 100.0
                }
            ]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200


def test_stock_decreases_after_sale(client):
    token = get_token(client)
    category_id = create_category(client, token, "Category Two")
    product_id = create_product(client, token, category_id, "SALE-002")

    # Check stock before sale
    product_before = client.get(f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    stock_before = product_before.json()["stock_quantity"]

    # Create sale with 5 items
    client.post("/sales/",
        json={
            "payment_method": "cash",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 5,
                    "unit_price": 100.0
                }
            ]
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    # Check stock after sale
    product_after = client.get(f"/products/{product_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    stock_after = product_after.json()["stock_quantity"]
    assert stock_after == stock_before - 5


def test_get_sales(client):
    token = get_token(client)
    response = client.get("/sales/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_sale(client):
    token = get_token(client)
    category_id = create_category(client, token, "Category Three")
    product_id = create_product(client, token, category_id, "SALE-003")
    create = client.post("/sales/",
        json={
            "payment_method": "card",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1,
                    "unit_price": 100.0
                }
            ]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    sale_id = create.json()["id"]
    response = client.get(f"/sales/{sale_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["id"] == sale_id


def test_delete_sale(client):
    token = get_token(client)
    category_id = create_category(client, token, "Category Four")
    product_id = create_product(client, token, category_id, "SALE-004")
    create = client.post("/sales/",
        json={
            "payment_method": "cash",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1,
                    "unit_price": 100.0
                }
            ]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    sale_id = create.json()["id"]
    response = client.delete(f"/sales/{sale_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200


def test_create_sale_without_token(client):
    response = client.post("/sales/",
        json={
            "payment_method": "cash",
            "items": []
        }
    )
    assert response.status_code == 401