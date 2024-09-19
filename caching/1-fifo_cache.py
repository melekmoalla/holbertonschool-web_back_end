#!/usr/bin/env python3

""" BaseCaching defines:
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ BaseCaching defines:
    Create a class FIFOCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """ function init
        """
        super().__init__()

    def put(self, key, item):
        """ function iputit
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                name = list(self.cache_data)[0]
                print('DISCARD:' + ' ' + name)
                self.cache_data.pop(name)

    def get(self, key):
        if key:
            return self.cache_data[key]
        else:
            return None
