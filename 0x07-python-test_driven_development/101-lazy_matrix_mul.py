<<<<<<< HEAD
#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
=======
#!/usr/bin/python3.5
"""

Module composed by a function that multiplies 2 matrices

"""
>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
import numpy as np


def lazy_matrix_mul(m_a, m_b):
<<<<<<< HEAD
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
=======
    """ Function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication


>>>>>>> ef0dafb725f1ce90803cd471edf8679638776c40
    """

    return (np.matmul(m_a, m_b))
