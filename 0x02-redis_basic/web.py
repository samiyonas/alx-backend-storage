#!/usr/bin/env python3
""" implementing an expiring web cache and tracker """
import requests
import redis
from functools import wraps
from typing import Callable


r = redis.Redis()

def cache_page(f: Callable) -> Callable:
    """ decorator that cache's how many times a url was requested """
    @wraps(f)
    def wrapper(url):
        """ wrapper function for f """

        r.incr(f"count:{url}")

        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")

        cached_html = f(url)
        r.setex(f"cached:{url}", 10, cached_html)

        return cached_html

    return wrapper


@cache_page
def get_page(url: str) -> str:
    response = requests.get(url)

    return response.text
