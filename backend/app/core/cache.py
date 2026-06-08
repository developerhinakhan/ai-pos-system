import redis
import json
from app.core.config import settings

# Connect to Redis using RESP2 protocol to support older Redis server versions
redis_client = redis.from_url(settings.REDIS_URL, protocol=2)


def get_cache(key: str):
    data = redis_client.get(key)
    if data:
        return json.loads(data)
    return None


def set_cache(key: str, value, expire: int = 300):
    redis_client.setex(key, expire, json.dumps(value, default=str))


def delete_cache(key: str):
    redis_client.delete(key)


def delete_pattern(pattern: str):
    keys = redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)