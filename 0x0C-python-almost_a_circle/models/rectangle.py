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
        """
        private attri width
        """
        return self.__width

    @width.setter
    def width(self, value):
         self.___width = value

    @property
    def height(self):
        """
        private attri width)
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, value):
        self.__x = value


