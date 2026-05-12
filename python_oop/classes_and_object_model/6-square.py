#!/usr/bin/env python3
"""Module that control how objects are represented as strings"""


class Square:
    """Class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # characters"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square"""
        result = ""
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            result += "\n"
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
