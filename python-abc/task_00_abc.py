#!/usr/bin/python3
"""Docstring Abstract animal class and its subclasses"""


from abc import ABC


class Animal(ABC):

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"