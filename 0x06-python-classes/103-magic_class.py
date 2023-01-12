#!/usr/bin/python3
<<<<<<< HEAD

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

=======
"""writing a docstring"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
import math


class MagicClass:
<<<<<<< HEAD
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
=======
    """set up the magic"""

    def __init__(self, radius=0):
        """ writing another docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """again with the docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """such docstring"""
        return 2 * math.pi * self.__radius
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
