#!/usr/bin/python3
"""
A class BasicCache that inherits from BaseCaching
and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class named BasicCache that inherits from class 
    BaseCaching
    """

    def put(self, key, item):
        """
        A function that assigns the  item value for the key of the 
        self.cache_data to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        A function that returns the value in self.cache_data
        that is linked to key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
