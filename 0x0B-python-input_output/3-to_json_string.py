#!/usr/bin/python3

"""The JSON string"""
import json
"""Returns JSON"""


def to_json_string(my_obj):
    """
    A function that returns the JSON
    representation of an object
    """
    return json.dumps(my_obj)
