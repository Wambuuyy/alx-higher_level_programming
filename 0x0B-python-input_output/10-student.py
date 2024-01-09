#!/usr/bin/python3
# 10-student.py
# Prudence wambui
"""
class called student based on 9-student.py
"""


class Student:
    """
    public instance attributes:
        first_name
        last_name
        age
    instantiation with first_name, last_name and age:
        def __init__(self, first_name, last_name, age):
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
