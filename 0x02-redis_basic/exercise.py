#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ A cache class that stores an instance of Redis client
    and writes string to Redis
    """
    def __init__(self):
        """ creates redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ writes a string to redis (the key is the string) """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, None, int, float]:
        """ gets you the decoded value of the key """
        value = self._redis.get(key)
        if not fn:
            return value
        return fn(value)

    def get_str(self, key: str) -> str:
        """ return string """
        value = self._redis.get(key)
        value = str(value.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """ return integer """
        value = self._redis.get(key)
        value = int(value.decode('utf-8'))
        return value
