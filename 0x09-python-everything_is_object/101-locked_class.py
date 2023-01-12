#!/usr/bin/python3
<<<<<<< HEAD
"""
Module for a class that prevents dynamic attributes creation

"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
=======
"""This defines a locked class"""


class LockedClass:
    """
    Only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
