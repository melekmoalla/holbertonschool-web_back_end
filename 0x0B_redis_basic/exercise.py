#!/usr/bin/env python3
"""
0x0B_redis_basic file
"""
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
