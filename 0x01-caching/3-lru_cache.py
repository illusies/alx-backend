#!/usr/bin/python3
"""
A class LRUCache that inherits from BaseCaching
and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A class named LRUCache that inherits from class 
    BaseCaching
    """

    def __init__(self):
        """A function that initializes the keys"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        A function that assigns the  item value for the key of the 
        self.cache_data to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        A function that returns the value in self.cache_data
        that is linked to key
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
