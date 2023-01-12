#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
=======
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        """
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Get/set the width of the Rectangle."""
=======
        """retrieves width attribute"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
=======
        """sets width attribute"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """Get/set the height of the Rectangle."""
=======
        """retrieves height attribute"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
=======
        """sets height attribute"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
<<<<<<< HEAD
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
=======
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

<<<<<<< HEAD
    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
=======
    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
