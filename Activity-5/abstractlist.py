"""
File: abstractlist.py
Copyright 2015 by Ken Lambert

Common data and method implementations for lists.
"""

from abstractcollection import AbstractCollection

class AbstractList(AbstractCollection):
    """Represents an abstract list."""

    def __init__(self, sourceCollection):
        """Maintains a count of modifications to the list."""
        AbstractCollection.__init__(self, sourceCollection)

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + " not in list.")

    def remove(self, item):
        """Precondition: item is in self.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        position = self.index(item)
        self.pop(position)

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)

    def append(self, item):
        """Adds the item to the end of the list."""
        self.add(item)

    def listIterator(self):
        """Returns a list iterator."""
        return AbstractList.ListIterator(self)

    class ListIterator(object):
        """Represents the list iterator for an array list."""

        def __init__(self, backingStore):
            """Sets the initial state of the list iterator."""
            self._backingStore = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store.
            lastItemPos is undefined."""
            self._cursor = 0
            self._lastItemPos = -1

        def hasNext(self):
            """Returns True if the iterator has a next item or False otherwise."""
            return self._cursor < len(self._backingStore)

        def next(self):
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasNext():
                raise ValueError("No next item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._lastItemPos = self._cursor
            self._cursor += 1
            return self._backingStore[self._lastItemPos]
           
        def last(self):
            """Moves the cursor to the end of the backing store."""
            self._cursor = len(self._backingStore)
            self._lastItemPos = -1

        def hasPrevious(self):
            """Returns True if the iterator has a previous item or False otherwise."""
            return self._cursor > 0

        def previous(self):
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._cursor -= 1
            self._lastItemPos = self._cursor
            return self._backingStore[self._lastItemPos]

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self._lastItemPos == -1:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self._backingStore[self._lastItemPos] = item
            self._lastItemPos = -1

        def insert(self, item):         
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self._lastItemPos == -1:
                self._backingStore.add(item)
            else:
                self._backingStore.insert(self._lastItemPos, item)
                self._lastItemPos = -1
            self._modCount += 1

        def remove(self):         
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position."""
            if self._lastItemPos == -1:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            item = self._backingStore.pop(self._lastItemPos)
            # If the item removed was obtained via next, move cursor back
            if self._lastItemPos < self._cursor:
                self._cursor -= 1
            self._modCount += 1
            self._lastItemPos = -1



