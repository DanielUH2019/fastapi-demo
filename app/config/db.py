import os
import redis


def create_redis() -> redis.ConnectionPool | None:
    REDIS_URL = os.getenv("REDIS_URL")

    if REDIS_URL:
        redis_client = redis.ConnectionPool.from_url(REDIS_URL)
    else:
        redis_client = None

    return redis_client


pool = create_redis()
