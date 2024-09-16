#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union


class Cache:
    """ A cache class that stores an instance of Redis clien
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
