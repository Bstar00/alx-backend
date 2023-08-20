#!/usr/bin/env python3
"""
This a Helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range function

    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and
        end indices for the specified page.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
