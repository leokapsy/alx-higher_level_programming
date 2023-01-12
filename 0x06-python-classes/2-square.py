#!/usr/bin/python3
<<<<<<< HEAD
"""class Square that defines a square"""


class Square():
    """square class with it's size and proper validation"""

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
=======
# 0-square.py by Ehoneah Obed
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        self.__size = size
