#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 Part 2 Module"""


class Book(object):
    """Creates a class with two attributes, author and title, which default to a blank string"""

    title = ""
    author = ""

    def __init__(self, title, author):
        self.title = title
        self.author = author


    def display(self):
        """Defines a function which prints out a string representing the book"""

        return "{}, written by {}".format(self.title, self.author)

BOOK1 = Book("Of Mice and Men", "John Steinbeck")
BOOK2 = Book("To Kill a Mockingbird", "Harper Lee")

print BOOK1.display()
print BOOK2.display()
