#!/usr/bin/env python3
"""Module for Rectangle class. Inherits from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry.
    Represents a rectangle using width and height."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.
        Validates width and height using integer_validator from BaseGeometry.
        width and height are private attributes.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
