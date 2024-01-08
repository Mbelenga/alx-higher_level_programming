#!/usr/bin/python3

"""contains my list"""

class MyList(list):
    """A subclass of list"""
    def print_sorted(self):
    """Prints the sorted list"""
    sort_the_list = sorted(self)
    print(sort_the_list)
