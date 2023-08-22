#!/usr/bin/python3
"""
MRU Caching (Most Recently Used)
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used (MRU) Cache class
    """

    def __init__(self):
        """
        Constructor
        """
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            # Update the time and associate it with the key
            self.timesKey[key] = self.time
            self.time += 1

            # Add the new item to the cache
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the key with the newest associated time
            # (i.e., most recently used)
            discard_key = max(self.timesKey, key=self.timesKey.get)

            # Remove the newest item from both the cache and timesKey
            del self.cache_data[discard_key]
            del self.timesKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """
        Retrieve the cache item value
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the time and associate it with the key
        self.timesKey[key] = self.time
        self.time += 1

        return self.cache_data[key]
