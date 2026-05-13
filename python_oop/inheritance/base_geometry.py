#!/usr/bin/env python3
""" Module for BaseGeometry class"""


class BaseGeometry:
    """ A class used to represent base geometry"""

    def area(self):
        raise Exception

    def integer_validator(self, name, value):
        """Validates values:
        - must be an integer (TypeError)
        - must be greater than 0 'ValueError)
        """
        if type(value) is not int:
            raise TypeError("{}must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}must be greater than 0".format(name))
