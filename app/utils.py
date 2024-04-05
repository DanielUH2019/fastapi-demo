from app.models import Criterion, Order  


def process_orders(orders: list[Order], criterion: Criterion) -> float:
    total_revenue = sum(
        order.quantity * order.price
        for order in orders
        if criterion == Criterion.all or order.status == criterion.value
    )
    return total_revenue