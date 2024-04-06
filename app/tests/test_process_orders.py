import math
import pytest
from app.models import Order, Criterion
from app.utils import process_orders


@pytest.mark.parametrize(
    "criterion,expected_output",
    [
        (Criterion.completed, 1299.69),
        (Criterion.pending, 999.9),
        (Criterion.canceled, 140.74),
        (Criterion.all, 2440.33),
    ],
)
def test_process_orders_criterions(
    criterion: Criterion, expected_output: float, orders: list[Order]
):
    result = process_orders(orders, criterion)
    assert math.isclose(result, expected_output)

