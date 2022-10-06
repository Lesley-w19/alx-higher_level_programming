#!/usr/bin/python3
# a function that divides element by element 2 lists. """


def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists. """
    newList = list()

    for l in range(list_length):
        try:
            newList.append(my_list_1[l] / my_list_2[l])
        except IndexError:
            newList.append(0)
            print("out of range")
        except TypeError:
            newList.append(0)
            print("wrong type")
        except ValueError:
            pass
        except ZeroDivisionError:
            newList.append(0)
            print("division by 0")
        finally:
            pass
    return newList
