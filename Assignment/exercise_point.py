import math
import time
from matplotlib import pyplot as plt


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

    def plot(self):
        """Plot the point"""
        plt.plot(self.x, self.y, 'bo')

    def get_line_to(self, provided_point):
        """Returns tulipe with coefficients of line y = ax + b connecting the provided point to the point """

        """Calculate slope"""
        a = (provided_point.y - self.y) / (provided_point.x - self.x)

        """Calculate b"""
        b = self.y - a * self.x

        return (a,b)



class smsStore:
    """ SMS tuple should contain:  (has_been_viewed, from_number, time_arrived, text_of_SMS)"""

    def __init__(self):
        """Create new inbox"""
        self.messages = [(False, '0031000000', time.gmtime(), 'Your new inbox has been created succesfully')]

    def add_new_arrival(self, number='0031000000', message=''):
        """Appends a new message to the inbox"""
        self.messages.append((False, number, time.gmtime(), message))

    def message_count(self):
        """Returns the number of sms messages in my_inbox """
        return len(self.messages)

    def get_unread_indexes(self):
        """Returns all unread messages"""
        for message in self.messages:
            if message[0] == False:
                return message

    def get_message(self, index):
        try:
            message = (self.messages[index][1],self.messages[index][2],self.messages[index][3])

            #Change read status to True
            self.messages.append((True, self.messages[index][1], self.messages[index][2], self.messages[index][3]))
            self.messages.pop(index)

            #Return(from_number, time_arrived, text_of_sms)
            return message

        except:
            return None

    def delete(self, index):
        self.messages.pop(index)
