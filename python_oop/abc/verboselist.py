#!/usr/bin/env python3
"""Module that extend the Python list"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))
