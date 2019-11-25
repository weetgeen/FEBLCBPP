"""Rewrite distance function from Fruitful functions"""
import math

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def reflect_x(self):
        """Returns a new point, which is a reflection of the provided point around the x-axis e.g.
            Point(3,5).reflect_x() is (3,-5)"""

        return Point(self.x, - self.y)

    def slope_from_origin(self):
        """Returns the slope of the line joining the origin to the point"""
        return round(math.degrees(abs(math.atan(self.y/self.x))), 2)

punt = Point(3,9)
reflection = punt.reflect_x()