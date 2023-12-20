#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for b in range(0, x):
        try:
            print("{:d}".format(my_list[b]), end="")
            index += 1
        except (TypeError, ValueError):
            pass
    print()
    return index
