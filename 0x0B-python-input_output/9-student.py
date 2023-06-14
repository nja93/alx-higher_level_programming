#!/usr/bin/python3

"""
create class Student
"""

class Student:
    """
    Defines a class Student 
    args:
        def __init__ - constructor
        def to_json
   
    """
    def __init__(self, first_name, last_name, age):
        """initializes the attributes of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
