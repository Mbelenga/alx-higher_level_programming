#!usr/bin/python3

"""
A function that returns the dictionary description with
simple data structure (List,Dictionary,string,integer
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """Define the function"""
    return obj.__dict__
