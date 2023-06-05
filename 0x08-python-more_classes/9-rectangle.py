#!/usr/bin/python3

"""Create a Rectangl Class"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """define width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """To retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """define the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """compute area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """compute perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """defines the print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets the del behavior of the Rectangle object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """returns the biggest rectangle based on the area"""
        if type(rect1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect1.area() >= rect2.area():
            return rect1
        else:
            return rect2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        width = size
        height = size
        return cls(width, height)
