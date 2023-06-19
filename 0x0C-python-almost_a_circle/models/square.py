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

    def update(self, *args, **kwargs):
        """assign  argument to each attribute"""
        if len(args):
            for arg, a in enumerate(args):
                if arg == 0:
                    self.id = a
                elif arg == 1:
                    self.size = a
                elif arg == 2:
                    self.x = a
                elif arg == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns dict representation of a Rectangle"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
            }
