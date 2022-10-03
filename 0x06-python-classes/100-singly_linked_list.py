#!/usr/bin/python3
""" a class Node that defines a node of a singly linked list """


class Node:
    """ a class Node that defines a node of a singly linked list """
    __data = 0
    __next_node = None

    def __init__(self, dData, nNode=None):
        self.data = dData
        self.next_node = nNode

    @property
    def data(self):
        """ to retrieve it and allow access """
        return self.__data

    @data.setter
    def data(self, value):
        """  to set it
        args: value is to be an integer
        Raises:
         TypeError: if value is not an integer
         """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ to retrieve and access it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, nValue=None):
        """ to set it
        args: value is equal to none or must be
        Raise:
        TypeError: next_node must be a Node object
        """
        if (nValue is not None and not isinstance(nValue, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = nValue


""" SinglyLinkedList"""


class SinglyLinkedList:
    """ a class SinglyLinkedList that defines a singly linked list """
    __head = None

    def __init__(self):
        pass

    def __str__(self):
        head = self.__head
        result = ""

        while (head is not None):
            result += str(head.data)
            if (head.next_node is not None):
                result += '\n'
            head = head.next_node
        return result

    def sorted_insert(self, value):
        new = Node(value)
        head = self.__head

        while (
            head is not None and
            head.next_node is not None and
            head.next_node.data < new.data
        ):
            head = head.next_node

        if head is None:
            self.__head = new
        else:
            new.next_node = head.next_node
            head.next_node = new
            if (head.data > new.data):
                tmp = new.data
                new.data = head.data
                head.data = tmp
