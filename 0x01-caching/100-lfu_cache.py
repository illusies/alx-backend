#!/usr/bin/python3
"""
A class LFUCache that inherits from BaseCaching
and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A class named LFUCache that inherits from class 
    BaseCaching
    """

    def __init__(self):
        """A function that initializes the keys"""
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """
        A function that assigns the  item value for the key of the 
        self.cache_data to the dictionary
        """
        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS and
                    key not in self.keys):
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.uses[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        """
        A function that returns the value in self.cache_data
        that is linked to key
        """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        """
        A function that returns key of the least frequently
        used item in cache
        """
        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
