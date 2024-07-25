#!/usr/bin/env python3
"""
Creates a class FIFOCache that inherits from BaseCaching
"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system class that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        return the value in self.cache_data
        """
        return self.cache_data.get(key, None)
