#!/usr/bin/env python3
"""Module for SHape abstract an dits subclasses"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class that defines the contract for geometric shapes"""
    @abstractmethod
    def area(self):
        """Returns the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape"""
        pass


class Circle(Shape):
    """Concrete class representing a circle"""
    def __init__(self, radius):
        """Initializes the circle with a radius"""
        self.radius = radius

    def area(self):
        """Returns the area of the circle"""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete class representing a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
