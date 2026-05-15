#!/usr/bin/env python3
"""Module for FlyingFish class using multiples inheritance"""


class Fish:
    """Class representing a fish"""

    def swim(self):
        """Prints that the fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish"""
        print("The fish lives in water")


class Bird:
    """Prints that the bird is flying """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish that inherits from Fish and Bird"""
    def swim(self):
        """Prints that the flying fish is swimming"""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints that the flying fish is soaring"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints the habitat of the flying fish"""
        print("The flying fish lives both in water and the sky!")
