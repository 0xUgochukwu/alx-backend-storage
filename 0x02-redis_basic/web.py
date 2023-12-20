#!/usr/bin/env python3
'''
    Redis Basics
'''
from typing import Callable
import redis
import requests
from functools import wraps


def track_requests(method: Callable) -> Callable:
    '''
        Decorator that counts the number of requests to a url
        and caches the responses for 10 seconds.
    '''

    @wraps(method)
    def wrapper(url: str) -> str:
        '''
            The wrapper function.
        '''
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = method(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_requests
def get_page(url: str) -> str:
    '''
        Gets a page content.
    '''
    return requests.get(url).text
