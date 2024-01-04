#!/usr/bin/python3
# 1-rectangle.py
"""defines a rectangle based on 0-rectangle.py"""


class Rectangle:
    """it contains two attributes(private)
    width and height and they are optional"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        property width to retrieve it
        Returns width(int) of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
        width (int): The width of the rectangle

        Raises:
        TypeError: If width is not an integer
        ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property height to retrieve it
        Returns height(int) of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle
        Attributes:
        height (int): The height of the rectangle
        Raises:
        TypeError: If height is not an integer
        ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
