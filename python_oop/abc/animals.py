#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines the contract for animal subclasses"""
    @abstractmethod
    def sound(self):
        """Returns the sound made by the animal"""
        pass


class Dog(Animal):
    """Class Dog that inherits from Animal"""
    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Class Cat that inherits from Animal"""
    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
