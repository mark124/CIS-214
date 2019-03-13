"""
File: arraybag.py
Copyright 2015 by Ken Lambert

"""

from arrays import Array
from abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self."""
        modCount = self.getModCount()
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            if modCount != self.getModCount():
                raise AttributeError("Illegal modification of backing store")
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._modCount = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Resize array if necessary
        if len(self) == len(self._items):
            tempArray = Array(len(self) * 2)
            for i in range(len(self)):
                tempArray[i] = self._items[i]
            self._items = tempArray
        self._items[len(self)] = item
        self._size += 1
        self.incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        self.incModCount()
        # Resize array if necessary
        if len(self) <= .25 * len(self._items) and \
           ArrayBag.DEFAULT_CAPACITY <= len(self._items) // 2:
            tempArray = Array(len(self._items) // 2)
            for i in range(len(self)):
                tempArray[i] = self._items[i]
            self._items = tempArray
        
        
