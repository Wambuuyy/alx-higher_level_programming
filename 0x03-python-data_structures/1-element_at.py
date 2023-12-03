#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrirves an element from a list
    just like c
    """
    if idx < 0 or idx >= len(my_list):
        return
    else:
        return my_list[idx]

