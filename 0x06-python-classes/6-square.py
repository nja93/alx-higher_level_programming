#!/usr/bin/python3
"""Define a class Square."""
class Square:
    def __init__(self, size=0, position=(0, 0))
        self.size = size
        self.position = pos

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set current position of the square."""
        return (self.__pos)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__pos = value

    def area(self):
                return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__pos[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__pos[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
