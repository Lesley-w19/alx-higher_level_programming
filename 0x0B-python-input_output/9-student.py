#!/usr/bin/python3
"""
 a class Student that defines a student by:
"""


class Student:
    """ class Student """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """_summary_
        Instantiation of class Student
        Args:
            first_name (_type_): _public classs attribute_
            last_name (_type_): _public classs attribute_
            age (_type_): _public classs attribute_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        that retrieves a dictionary representation of
        a Student instance
        """
        return self.__dict__
