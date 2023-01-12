#!/usr/bin/python3
<<<<<<< HEAD
"""class Square that defines a square"""


class Square():
    """square class with it's size and proper validation"""

    def __init__(self, size=0):
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

    @property
    def size(self):
<<<<<<< HEAD
=======
        """Retrieves size of square"""

>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        return self.__size

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
=======
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
