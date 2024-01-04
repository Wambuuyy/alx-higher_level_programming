#!/usr/bin/python3
#7-rectangle.py
"""defines a rectangle based on 6-rectangle.py"""


class Rectangle:
    """
    It contains:
        two public class attributes: 
            number_of_instances
            print_symbol
        two private and optional attributes:
            width
            height
    """
    number_of_instances = 0;
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
    def __str__(self):
        """
        return a printable representation of the rectangle
        this case we use #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        #handle rows
        for rows in range(self.__height):
            #handle columns
            for columns in range(self.__width):
                string += str(Rectangle.print_symbol)
            #to go to the next row with a newline
            if i < (self.__height - 1):
                string += '\n'
        return string
    def __repr__(self):
        """
        provides a repr() for the object rectangle
        returns a string representation of the rectangle enabling it to be recreated using eval
        """
        return f"Rectangle({self.__width}, {self.__height})"
    def __del__(self):
        """the number of instances are decremented and it desplays a message once a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
