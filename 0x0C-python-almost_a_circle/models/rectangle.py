#!/usr/bin/python3

""""
import a class Base
"""

from models.base import Base


class Rectangle(Base):
    """initialize the Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrive attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """setting and validating"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieve """
        return self.__x

    @x.setter
    def x(self, value):
        """set and validate x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting and validating y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        computes area
        """
        return self.width * self.height

    def display(self):
        """
        prints result using # in std out
        """
        for t in range(self.__y):
            print()
        for h in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width), end="")
            print()

    def __str__(self):
        """
        String representation of rec`
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"assign argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if (args):
            for arg in range(len(args)):
                setattr(self, up[arg], args[arg])

        else:
            for kwa in kwargs:
                setattr(self, kwa, kwargs[kwa])

    def to_dictionary(self):
        """Returns the dict representation of a Rectangle"""
        return {
            "x": self.x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            'width': self.__width,
        }
