#!/usr/bin/env python3
"""
Basic caching script
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching system that inherits from BaseCaching.
    """

    def __init__(self):
        """
        Constructor for initializing the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
