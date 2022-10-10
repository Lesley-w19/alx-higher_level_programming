#!/usr/bin/python3
"""
 a class Student that defines a student by:
"""


class Student:
    """ class Student with public attributes"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """ constructor of instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_
        that retrieves a dictionary representation of a Student instance
        Args:
            attrs (_type_, optional): . Defaults to None.
            _description_
            if attrs is a list of strings, only attribute names
            contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        data_obj = {}

        if None is attrs:
            return self.__dict__

        for att in attrs:
            if type(att) is not str:
                continue
            if hasattr(self, att):
                data_obj[att] = getattr(self, att)
        return data_obj

    def reload_from_json(self, json):
        """_summary_
        that replaces all attributes of the Student instance:
        Args:
            json (_type_): will always be a dictionary
        """
        for key in json.keys():
            self.__dict__[key] = json[key]
