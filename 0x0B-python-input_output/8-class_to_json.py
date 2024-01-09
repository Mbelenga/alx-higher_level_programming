#!usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structure (List,Dictionary,string,integer
    and boolean) for JSON serialization of an object
    """
    return obj.__dict__
