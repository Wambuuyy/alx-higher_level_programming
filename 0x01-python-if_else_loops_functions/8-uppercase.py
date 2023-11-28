#!/usr/bin/python3


def uppercase(str):
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:  #check if liwercase
            char_code -= 32  #convert upper
        print("{:c}".format(char_code), end="")
    print()
