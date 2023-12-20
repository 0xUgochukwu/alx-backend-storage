#!/usr/bin/env python3
'''
    Redis Basics
'''
from typing import Callable
import redis
import requests
from functools import wraps


cache = redis.Redis()


def count_requests(method: Callable) -> Callable:
    '''
        Decorator that counts the number of requests to a url
        and caches the responses for 10 seconds.
    '''

    @wraps(method)
    def wrapper(url):
        '''
            The wrapper function.
        '''
        cache.incr(f'count:{url}')
        cached_res = cache.get(f'cached:{url}')
        if cached_res:
            return cached_res.decode('utf-8')
        res = method(url)
        cache.setex(f'cached:{url}', 10, res)
        return res
    return wrapper


@count_requests
def get_page(url: str) -> str:
    '''
        Gets a page content.
    '''
    return requests.get(url).text
