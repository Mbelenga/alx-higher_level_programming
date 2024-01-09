#!usr/bin/python3

"""Reads a text file"""

def read_file(filename=""):

    with open (filename, 'r' , encoding='utf8') as file:

        content = file.read()
    print(content)
