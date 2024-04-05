from fastapi import FastAPI

from app.models import Criterion, Order
from app.utils import process_orders


api = FastAPI()

@api.post("/solution")
def solution(orders: list[Order], criterion: Criterion = Criterion.all) -> float:
    return process_orders(orders, criterion)
