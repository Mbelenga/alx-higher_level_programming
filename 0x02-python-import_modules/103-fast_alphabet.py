#!/usr/bin/python3

import string
print(getattr(string, 'ascii_lowercase').upper().replace(getattr(string, 'ascii_lowercase')[0], ''))
