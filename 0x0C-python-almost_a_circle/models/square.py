#!/usr/bin/bash
# square.py
# Prudence Wambui
"""
created on 14/01/2024
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
    it inherits from rectangle
    width and height from the rectangle class are assigned as size
    no new attributes for the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        and assign key/value arguments to attributes"""
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns a dictionary of a square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
               }
