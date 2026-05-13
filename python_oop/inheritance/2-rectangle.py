#!/usr/bin/env python3
"""
Module for Rectangle class.
Inherits from BaseGeometry (task 1-rectangle).
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with private width and height.
        Validated by the parent's integer_validator.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.
        Overrides the area() method in BaseGeometry.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        Format: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
