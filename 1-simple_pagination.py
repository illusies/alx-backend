#!/usr/bin/env python3
"""
A program that contains a method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10
that returns an empty list if the input arguments are out of range for the dataset
"""


import csv
import math
from typing import List


class Server:
    """ Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        """A function that returns the correct list of rows"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        indexes = index_range(page, page_size)
        try:
            return self.dataset()[indexes[0]:indexes[1]]
        except IndexError:
            return []

def index_range(page: int, page_size: int) -> tuple:
    """A function that returns a tuple"""
    return ((page - 1) * page_size, page * page_size)
