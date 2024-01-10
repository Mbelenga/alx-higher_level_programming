#!/usr/bin/python3

"""A class student"""


class student:
    def __init__(self, first_name, last_name, age):
        """Public instance with attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary"""
        return (self.__dict__)
