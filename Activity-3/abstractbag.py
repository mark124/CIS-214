"""
File: abstractbag.py
Copyright 2015 by Ken Lambert

"""

from abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    """Repository for common bag data and methods."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods

    def __str__(self):
        """Returns the string rep of the bag."""
        result = AbstractCollection.__str__(self)
        return "{" + result[1:-1] + "}"

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
