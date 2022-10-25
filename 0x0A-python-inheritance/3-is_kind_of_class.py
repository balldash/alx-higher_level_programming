#!/usr/bin/python3
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """Method for comparing object classes

        Args:
            obj (unknown): object whose type is to be checked.
            a_class (str): class criteria to validate.

        Return:
            True if obj is isinstance of a_class
            other False

    """

    if issubclass(type(obj), a_class) or isinstance(obj, a_class):
        return True
    return False
