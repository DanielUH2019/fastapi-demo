import math
import pytest
from fastapi.testclient import TestClient

from app.main import api
from app.models import Order

client = TestClient(api)


def test_solution_with_valid_orders(orders: list[Order]):
    response = client.post(
        "/solution",
        json={
            "orders": [o.model_dump() for o in orders],
            "criterion": "completed",
        },
    )
    assert response.status_code == 200
    assert math.isclose(response.json(), 1299.69)


def test_solution_with_negative_price_orders():
    orders_with_negative_price = [
        {
            "id": 1,
            "item": "Laptop",
            "quantity": 1,
            "price": -999.99,
            "status": "completed",
        },
        {
            "id": 2,
            "item": "Smartphone",
            "quantity": 2,
            "price": -499.95,
            "status": "pending",
        },
        {
            "id": 3,
            "item": "Headphones",
            "quantity": 3,
            "price": -99.90,
            "status": "completed",
        },
    ]
    response = client.post(
        "/solution", json={"orders": orders_with_negative_price, "criterion": "all"}
    )
    assert response.status_code == 422


def test_solution_with_zero_quantity_orders():
    orders_with_zero_quantity = [
        {
            "id": 1,
            "item": "Laptop",
            "quantity": 0,
            "price": 999.99,
            "status": "completed",
        },
        {
            "id": 2,
            "item": "Smartphone",
            "quantity": 0,
            "price": 499.95,
            "status": "pending",
        },
        {
            "id": 3,
            "item": "Headphones",
            "quantity": 0,
            "price": 99.90,
            "status": "completed",
        },
    ]
    response = client.post(
        "/solution", json={"orders": orders_with_zero_quantity, "criterion": "all"}
    )
    assert response.status_code == 422

def test_solution_with_empty_orders():
    response = client.post("/solution", json={"orders": [], "criterion": "completed"})
    assert response.status_code == 200
    assert response.json() == 0