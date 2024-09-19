#!/usr/bin/env python3

""" LIFOCache defines:
A class that inherits from BaseCaching and is a LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching System """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # List to keep track of the order of insertion

    def put(self, key, item):
        """ Add an item to the cache """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)  # Remove key from order if it already exists

            self.cache_data[key] = item
            self.order.append(key)  # Add the key to the end of the order list

            # If cache exceeds the maximum number of items, discard the last added item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)  # Remove the second-last item (LIFO)
                print(f"DISCARD: {last_key}")
                del self.cache_data[last_key]

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
