#!/usr/bin/env python3
'''
    Redis Basics
'''
from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
        Decorator Function that counts the number of calls.
    '''

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            Wrapper function.
        '''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper




class Cache:
    ''' Cache class '''

    def __init__(self):
        '''
            Initialize cache data.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            Store data in cache.
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
            Get data from cache.
        '''
        data = self._redis.get(key)

        if fn:
            data = fn(data)

        return data

    def get_str(self, key: str) -> str:
        '''
            Get string from cache.
        '''
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        '''
            Get int from cache.
        '''
        data = self._redis.get(key)

        try:
            data = int(data.decode('utf-8'))
        except Exception:
            data = 0

        return data
