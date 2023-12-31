#!/usr/bin/python3

"""A module square"""


class Square:
    """
    Defines a class
    it checks for the data
    type and has  private attribute
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
