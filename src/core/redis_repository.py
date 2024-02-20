import json

import redis.asyncio as redis
from core.exceptions import RequestProcessingException
from core.settings import SETTINGS


class RedisRepository:
    __redis = None

    @classmethod
    async def connect_to_redis(cls):
        if cls.__redis is None:
            RedisRepository.__redis = await redis.from_url(
                SETTINGS.REDIS_URL, decode_responses=True
            )

    @classmethod
    async def set_to_redis(cls, key, value, expire_seconds=None):
        try:
            serialized_value = json.dumps(value)
            if expire_seconds is None:
                await cls.__redis.set(key, serialized_value)
            else:
                await cls.__redis.setex(key, expire_seconds, serialized_value)
        except redis.RedisError:
            raise RequestProcessingException

    @classmethod
    async def get_from_redis(cls, key):
        try:
            json_value = await cls.__redis.get(key)
            if json_value is not None:
                return json.loads(json_value)
        except redis.RedisError:
            raise RequestProcessingException

    @classmethod
    async def clear_key(cls, key):
        try:
            await cls.__redis.delete(key)
        except redis.RedisError:
            raise RequestProcessingException
