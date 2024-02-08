import json
from typing import List

import redis.asyncio as redis
from fastapi.encoders import jsonable_encoder

from src.core import settings
from src.core.exceptions import RequestProcessingException


class RedisRepository:
    __redis = None

    @classmethod
    async def connect_to_redis(cls):
        if cls.__redis is None:
            cls.__redis = await redis.from_url(
                settings.REDIS_URL, decode_responses=True
            )

    @classmethod
    async def clear_key(cls, key: str):
        try:
            await cls.__redis.delete(key)
        except redis.RedisError:
            raise RequestProcessingException

    @classmethod
    async def set_value(cls, key: str, value: List) -> None:
        try:
            jsonable_entities = [jsonable_encoder(entity) for entity in value]
            json_value = json.dumps(jsonable_entities)
            await cls.__redis.set(key, json_value)
        except redis.RedisError:
            raise RequestProcessingException

    @classmethod
    async def get_value(cls, key: str):
        try:
            json_value = await cls.__redis.get(key)
            if json_value is not None:
                return json.loads(json_value)
        except redis.RedisError:
            raise RequestProcessingException
