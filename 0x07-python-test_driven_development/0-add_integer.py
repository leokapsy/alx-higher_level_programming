#!/usr/bin/python3
<<<<<<< HEAD
"""Module containing a dummy adder function for testing"""


def add_integer(a, b=98):
    """ adds integers
        Arguments:
        @a: first integer
        @b: second integer, defaults to 98 if not given
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
=======
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
