#!/usr/bin/python3

"Create an object from JSON file"

import json
"Provides a function needed for converting"


def load_from_json_file(filename):
    "A function that creates an object from a JSON file"
    with open(filename "w") as file:
        return json.loads(my_str)
