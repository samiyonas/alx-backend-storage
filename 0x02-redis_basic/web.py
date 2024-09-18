#!/usr/bin/env python3
""" implementing an expiring web cache and tracker """
import requests
import redis


def cache_page(f):
    """ decorator that cache's how many times a url was requested """
    @wraps(f)
    def wrapper(*args, **kwargs):
        """ wrapper function for f """
        r = redis.Redis()
        count = "count:" + args[0]

        r.incr(count)

        cached_html = r.get("cached:" + args[0])
        if cached_html:
            return cached_html.decode("utf-8")

        cached_html = f(*args, **kwargs)
        r.setex("cached:" + args[0], 10, cached_html)

        return cached_html

    return wrapper


@cache_page
def get_page(url: str) -> str:
    response = requests.get(url)

    return response.text
