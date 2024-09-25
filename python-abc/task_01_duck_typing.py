#!/usr/bin/python3
"""Docstring shapes, interface and duck typing"""


from abc import ABC
import math


class Shape(ABC):

    def area(self):
        pass

    def perimeter(self):
        pass

class circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    

def shape_info(shape):
    print(f"area: {shape.area():.2f}")
    print(f"perimeter: {shape.perimeter():.2f}")