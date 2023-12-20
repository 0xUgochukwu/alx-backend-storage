#!/usr/bin/env python3
'''
    Redis Basics
'''
from typing import Union
from uuid import uuid4
import redis


class Cache:
    ''' Cache class '''

    def __init__(self):
        '''
            Initialize cache data.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
            Store data in cache.
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
