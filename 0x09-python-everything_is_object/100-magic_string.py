#!/usr/bin/python3
<<<<<<< HEAD
def magic_string(l=[]):
    l += ["BestSchool"]
    return ", ".join(l)
=======
def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.count)])
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
