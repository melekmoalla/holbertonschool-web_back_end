#!/usr/bin/env python3

""" BaseCaching defines:
Create a class LRUCache that inherits from
BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
                items = list(self.cache_data.items())
                items.insert(0, (key, item))
                self.cache_data = dict(items)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data)[0]
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")

                items = list(self.cache_data.items())
                items.insert(0, (key, item))
                self.cache_data = dict(items)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ function get
        """
        if key and key in self.cache_data:
            if key in self.cache_data:
                items = list(self.cache_data.items())
                items.insert(0, (key, self.cache_data[key]))
                self.cache_data = dict(items)
            return self.cache_data[key]
        else:
            return None
