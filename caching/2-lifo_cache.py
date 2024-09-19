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
        if key is None or item is None:
                    return
                
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # LIFO eviction: remove the last inserted item
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ function get
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
