#!usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with
    simple data structure (List,Dictionary,string,integer
    and boolean) for JSON serialization of an object
    args:
        obj:is an instance of a class
        All attributes of the object class are serializable
    """
    return obj.__dict__
