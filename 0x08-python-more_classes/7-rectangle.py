#!/usr/bin/python3

"""Create a Rectangle class that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve  width attribute"""
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
        """Retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Compute area the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Compute perimeter  of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """Define print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Return  string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Define the del behavior of the Rectangle object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
