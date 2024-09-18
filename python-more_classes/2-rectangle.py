#!/usr/bin/python3
"""Define a Rectangle class"""

class Rectangle:
    """defines the rectangle area and perimetre"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle
        
        Args:
        widht (int): widht of the rectangle
        height (int): height of the rectangle
        """
        self.widht = width
        self.height = height

    @property
    def width(self, value):
        """Get the widht of the rectangle"""
        return self.__width
    
    @width.setter
    def widht(self, value):
        """
        Set the width of the rectangle
        
        Args:
        value (int): the width is not integer
        
        Raises:
        TypeError: If width is not integer;
        ValueError: If width is less than 0;
        """
        if not isinstance(value, int):
            raise TypeError("width be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        
        Args:
        value (int): the height of the rectangle
        
        Raises:
        TypeError: If height is not integer.
        ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height
    
    def perimeter(self):
        """Return the rectangle perimeter"""
        if (self.__width == 0 and self.__height == 0):
            return (0)
        else:    
            return self.__width + self.__height
        