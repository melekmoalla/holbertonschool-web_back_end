#!/usr/bin/env python3

""" BaseCaching defines:
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCaching defines:
    Create a class FIFOCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """ function init
        """
        super().__init__()

    def put(self, key, item):
        """ function put
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                name = list(self.cache_data)[3]
                print('DISCARD:' + ' ' + name)
                self.cache_data.pop(e)
                

    def get(self, key):
        """ function get
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
