#!/usr/bin/env python3
"""Module for The Mystical Dragon using mixins method"""


class SwimMixin:
    """Mixin that provides swimming behavior"""

    def swim(self):
        """Prints that the creature is swimming"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior"""
    def fly(self):
        """Prints that the creature is flying"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that inherits from SwimMixin adn FlyMixin"""

    def roar(self):
        """Prints that the dragon is roaring"""
        print("The dragon roars!")
