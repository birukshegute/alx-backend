#!/usr/bin/env python3
"""
declares a function named index_range
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a function that returns a list for particular pagination parameter
    """
    startIndex = page * page_size
    return startIndex - page_size, startIndex
