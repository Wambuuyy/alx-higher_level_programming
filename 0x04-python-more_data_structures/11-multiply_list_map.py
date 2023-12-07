#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number if number != 0 else 0, my_list))
