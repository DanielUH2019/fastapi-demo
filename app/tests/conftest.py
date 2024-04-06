import pytest
from app.models import Order, Status


@pytest.fixture
def orders() -> list[Order]:
    return [
        Order(id=1, item="Laptop", quantity=1, price=999.99, status=Status.completed),
        Order(id=2, item="Smartphone", quantity=2, price=499.95, status=Status.pending),
        Order(
            id=3, item="Headphones", quantity=3, price=99.90, status=Status.completed
        ),
        Order(id=4, item="Mouse", quantity=4, price=24.99, status=Status.canceled),
        Order(id=5, item="Keyboard", quantity=1, price=27.00, status=Status.canceled),
        Order(id=6, item="Monitor", quantity=1, price=13.78, status=Status.canceled),
    ]
