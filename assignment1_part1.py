#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 Part 1 Module"""


def listDivide(numbers, divide=2):
    """Defines a function to return the number of elements in a list that are divisible by the second parameter

    Args:
        numbers (list): a list of numbers to be checked
        divide (int): an integer to divide the numbers in the list, default value of 2

    Returns:
        int: number of elements in the numbers list that are divisible by divide"""

    count = 0

    for i in numbers:
        if i % divide == 0:
            count += 1

    return count

class ListDivideException(Exception):
    pass

def testListDivide():
    """Defines a function to test if the listDivide function is working properly"""

    if listDivide([1,2,3,4,5]) == 2:
        pass
    else:
        raise ListDivideException
    if listDivide([2,4,6,8,10]) == 5:
        pass
    else:
        raise ListDivideException
    if listDivide([30,54,63,98,100], 10) == 2:
        pass
    else:
        raise ListDivideException
    if listDivide([]) == 0:
        pass
    else:
        raise ListDivideException
    if listDivide([1,2,3,4,5], 1) == 5:
        pass
    else:
        raise ListDivideException