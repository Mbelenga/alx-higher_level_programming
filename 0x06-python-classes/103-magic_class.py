#!/usr/bin/python3

"""Writing a python magic class matching a bytecode provided"""

import math


class MagicClass:
    """
    Define the area and circumference
    to represent the circle
    """
    def __init__(self, radius=0):
        """
        Initializing the MagicClass.
        Arguments:
            radius of MagicClass.
            """
            self.__radius = 0

            #  verify that radius is a number
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        #  update attribute
        self.__radius = radius

    def area(self):
        """
        Returns the area of our MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of our MagicClass.
        """
        return 2 * math.pi * self.__radius
