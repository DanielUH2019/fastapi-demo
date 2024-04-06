from typing import Annotated
from fastapi import Body, FastAPI

from app.models import Criterion, Order
from app.utils import process_orders


api = FastAPI()

@api.post("/solution")
def solution(orders: list[Order], criterion: Annotated[Criterion, Body()]) -> float:
    return process_orders(orders, criterion)
