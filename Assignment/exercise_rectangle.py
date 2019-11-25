import exercise_point

class Rectangle:
    """A class to manufacture rectangle objects"""

    def __init__(self, posn, width, height):
        """Injtialize rectangle at posn, with width and height as specified"""
        self.corner = posn
        self.width = width
        self.height = height

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width , self.height)


box = Rectangle(exercise_point.Point(0,0) , 100, 200)
