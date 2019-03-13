"""
File: linkedstack.py
Copyright 2015 by Ken Lambert

"""

from abstractstack import AbstractStack
from node import Node

class LinkedStack(AbstractStack):
    """Represents a link-based stack."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._head = None
        AbstractStack.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        lyst = list()
        probe = self._head
        while probe != None:
            lyst.append(probe.data)
            probe = probe.next
        lyst.reverse()
        modCount = self.getModCount()
        cursor = 0
        while cursor < len(lyst):
            yield lyst[cursor]
            if modCount != self.getModCount():
                raise AttributeError("Illegal modification of backing store")
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._head.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = None
        self._modCount = 0

    def push(self, item):
        """Inserts item at top of the stack."""
        self._head = Node(item, self._head)
        self._size += 1
        self.incModCount()

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        self._size -= 1
        self.incModCount()
        data = self._head.data
        self._head = self._head.next
        return data
