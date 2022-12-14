#!/usr/bin/python3
"""Module for Base class."""

class Base:
    """A description of the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nd_objexts += 1
            self.id = Base.__nb_objects
