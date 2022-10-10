#!/usr/bin/python3
"""
a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str, optional): file being read. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): _description_. Defaults to "".
    """

    new = ""

    with open(filename, 'r') as file:
        for new_line in file:
            new += new_line
            if search_string in new_line:
                new += new_string

    with open(filename, 'w') as file:
        file.write(new)
