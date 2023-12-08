#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmporary = my_dict.copy()
    for i, val in tmporary.items():
        if value == val:
            my_dict.pop(i)
    return my_dict
