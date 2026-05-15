#!/usr/bin/env python3
"""Module for Square class"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes Square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """String representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
