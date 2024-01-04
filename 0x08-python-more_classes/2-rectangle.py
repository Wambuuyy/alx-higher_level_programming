#!/usr/bin/python3
#2-rectangle.py
"""defines a rectangle based on 1-rectangle.py"""


class Rectangle:
    """it contains two attributes(private) width and height and they are optional"""
   def  __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    @property
    def height(self):
        """
        property height to retrieve it
        Returns height(int) of the rectangle
        """
        return self.__height
    @height.setter
    """
    Setter height of the rectangle
    Attributes:
    height (int): The height of the rectangle
    Raises:
    TypeError: If height is not an integer
    ValueError: If height is less than 0
    """
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def width(self):
        """
        property width to retrieve it
        Returns width(int) of the rectangle
        """
        return self.__width
    @width.setter
    """
    Setter width of the rectangle

    Attributes:
    width (int): The width of the rectangle

    Raises:
    TypeError: If width is not an integer
    ValueError: If width is less than 0
    """
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def area(self):
        """finds the area of the rectangle"""
        return self.__height * self .__width
    def perimeter(self):
        """finds he distance around the rectangle"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

