#!/usr/bin/env python3

""" BaseCaching defines:
Create a class LFUCache that inherits from
BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ BaseCaching defines:
    Create a class LFUCache that inherits from
    BaseCaching and is a caching system:
    """

    def __init__(self):
        """ function init
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """ function put
        """
        if key and item:
            if key in self.cache_data:
                self.freq[key] += 1
                self.cache_data[key] = item

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                temp = min(self.freq.values())
                res = [key for key in self.freq if self.freq[key] == temp]
                self.freq[key] = 1
                self.cache_data[key] = item
                print(f"DISCARD: {res[0]}")
                del self.freq[res[0]]
                del self.cache_data[res[0]]
            else:
                self.freq[key] = 1
                self.cache_data[key] = item

    def get(self, key):
        """ function get
        """
        if key and key in self.cache_data:
            if key in self.cache_data:
                self.freq[key] += 1

            return self.cache_data[key]
        else:
            return None
