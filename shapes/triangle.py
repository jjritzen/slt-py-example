#!/usr/bin/env python

"""
Author: Jan-Joep Ritzen
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains 3 sides (a, b and c).
    """

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        """
        Compute the area using the formula (a * b)/2
        """
        return (self.a * self.b)/2

    def perimeter(self):
        """
        Compute the perimeter using the formula (a + b + c)
        """
        return (self.a + self.b + self.c)

    def is_right(self):
        """
        Determine if the triangle is a right triangle by comparing the length
        and width for equality. 
        """
        return self.c**2 == self.a**2 + self.b**2
