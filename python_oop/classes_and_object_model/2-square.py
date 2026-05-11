#!/usr/bin/env python3
"""Module that add validation to the size attribute on the Square class"""


class Square:
    """Class that represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
