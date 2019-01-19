"""
Functions for computing areas of various shapes
"""
import math


def triangle_area(height, base):

    """
    Compute the area of a triangle with the given height and base.
    Raises a ValueError if either height or base are negative.
    """

    if height < 0 or base < 0:
        raise ValueError('Base and height must be positive.')
    return height * base * 0.5


def circle_area(radius):
    """
    Compute the area of a circle.
    Raises a ValueError if the radius is negative
    """
    if radius < 0:
        raise ValueError
    return radius ** 2 * math.pi
