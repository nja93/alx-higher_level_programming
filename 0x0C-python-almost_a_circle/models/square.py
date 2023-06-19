#!/usr/bin/python3
"""imports from Rectangle class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """class square created as a subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(size, size, x, y, id)

    def __str__(self):
    """
    String representation of square
    """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
    """
    Get size attribute
    """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
