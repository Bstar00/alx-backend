#!/usr/bin/python3
"""
Basic dictionary script
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    The caching system class
    """

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value of a cache item
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
