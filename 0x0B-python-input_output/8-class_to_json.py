#!/usr/bin/python3
# 8-class_to_json.py
# Prudence Wambui
"""
funtion that returns the dictionary
description with simple data structure
for json serialization of an object
"""


def class_to_json(obj):
    """
    obj is an instance to a class
    all attributes of the obj Class are serializable:
        list, boolean, string, integer, dictionary

    get all attributes of the object
    convert them to serializable form / decodable form
    """
    attributes = obj.__dict__
    serialized_attributes = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_attributes[key] = value
    return serialized_attributes
