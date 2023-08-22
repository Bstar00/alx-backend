#!/usr/bin/python3
"""
FIFO caching implementation
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First-In-First-Out (FIFO) Cache implementation
    """

    def __init__(self):
        """
        Constructor for initializing the cache
        """
        self.order = []
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO strategy
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.order[0]
            del self.cache_data[discard]
            del self.order[0]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        Retrieve the value associated with a key from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
