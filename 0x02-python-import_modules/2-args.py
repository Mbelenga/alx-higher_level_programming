#!/usr/bash/python3
if __name__ == '__main___':
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format('0'))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} arguments:".format(count))

    for i in range(count):
        print("{}: {}".format(i + i, sys.argv[i + 1]))
