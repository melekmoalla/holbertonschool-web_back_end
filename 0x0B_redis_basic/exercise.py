#!/usr/bin/env python3
"""
0x0B_redis_basic file
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, result)

        return result
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        data = self._redis.get(key)
        return self._decode_utf8(data) if data else None

    def get_int(self, key: str) -> Optional[int]:
        data = self._redis.get(key)
        return int(data) if data else None

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


def replay(method: Callable):
    method_name = method.__qualname__
    cache_instance = method.__self__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    call_count = cache_instance._redis.get(method_name)
    if call_count:
        call_count = int(call_count)
    else:
        call_count = 0

    print(f"{method_name} was called {call_count} times:")

    inputs = cache_instance._redis.lrange(input_key, 0, -1)
    outputs = cache_instance._redis.lrange(output_key, 0, -1)

    for input_args, output in zip(inputs, outputs):
        input_str = input_args.decode("utf-8")
        output_str = output.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")
