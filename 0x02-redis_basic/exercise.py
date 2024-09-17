#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ store history of inputs and outputs for particular function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ a wrapper function for methods of Cache class """
        inputs = method.__qualname__ + ":inputs"
        outputs = method.__qualname__ + ":outputs"

        self._redis.rpush(inputs, *map(str, args))
        result = method(self, *args, **kwargs)

        self._redis.rpush(outputs, result)

        return result
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ a decorator that takes a function as an argument """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ a wrapper function for methods of the Cache class """
        key = method.__qualname__
        if self._redis.exists(key):
            self._redis.incr(key)
        else:
            self._redis.set(key, 1)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ A cache class that stores an instance of Redis client
    and writes string to Redis
    """
    def __init__(self):
        """ creates redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
