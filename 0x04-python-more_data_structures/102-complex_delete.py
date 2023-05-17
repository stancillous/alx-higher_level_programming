#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for k, v in a_dictionary.items():
        if v == value:
            key_list.append(k)
    for i in key_list:
        del a_dictionary[i]
    return (a_dictionary)
