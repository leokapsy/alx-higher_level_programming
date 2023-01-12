#!/usr/bin/python3
<<<<<<< HEAD
"""Module containing a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: first name to be printed
            @second_name: last_name to be printed
=======
"""

This module is composed by a function prints a message

"""


def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"

    Args:
        first_name: first name
        last_name: last name

    Returns:
        No return

    Raises:
        TypeError: If first_name or last_name is not a string


>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
<<<<<<< HEAD
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
=======

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
    print("My name is {} {}".format(first_name, last_name))
