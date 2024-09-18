#!/usr/bin/evn python3
""" implementing an expiring web cache and tracker """
import requests
import redis


def cache_page(f):
    """ decorator that cache's how many times a url was requested """
    @wraps(f)
    def wrapper(*args, **kwargs):
        """ wrapper function for f """
        r = redis.Redis()
        key = "count:" + args[0]

        result = f(*args, **kwargs)

        if r.exists(key):
            r.incr(key, ex=10)
        else:
            r.set(key, 1, ex=10)
        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    response = requests.get("http://slowwly.robertomurray.co.uk")

    return response.text
