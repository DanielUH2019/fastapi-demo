from typing import Annotated
from fastapi import Body, FastAPI, Depends

from app.models import Criterion, Order
from app.utils import process_orders
from app.config.db import pool
import redis


def get_redis() -> redis.Redis | None:
    # Here, we re-use our connection pool
    # not creating a new one
    if pool:
        return redis.Redis(connection_pool=pool)

    return None


api = FastAPI()


@api.post("/solution")
def solution(
    orders: list[Order],
    criterion: Annotated[Criterion, Body()],
    cache: redis.Redis | None = Depends(get_redis),
) -> float:
    if cache:
        cache_key = f"{criterion.value}:{hash(tuple((x.id for x in orders)))}"
        cached_result = cache.get(cache_key)
        if cached_result:
            print("Cache hit")
            return float(cached_result)

    result = process_orders(orders, criterion)
    if cache:
        cache.setex(cache_key, 3600, str(result))
    return result
