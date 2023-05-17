#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    for key in sorted(a_dictionary):
        new_dict[key] = a_dictionary[key]

    for i, j in new_dict.items():
        print("{}: {}".format(i,j))
