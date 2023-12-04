#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i not in "cC":
            new_str += i
    return (new_str)
