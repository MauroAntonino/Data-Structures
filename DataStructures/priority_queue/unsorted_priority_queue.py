from DataStructures.priority_queue.base import PriorityQueueBase
from DataStructures.linked_lists.positional_list import PositionalList

class UnsortedPriorityQueue(PriorityQueueBase): # base class defines Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self): # nonpublic utility
        """Return Position of item with minimum key."""
        if self.is_empty( ): # is empty inherited from base class
            raise Exception('Priority queue is empty')
        small = self._data.first( )
        walk = self._data.after(small)
        while walk is not None:
            if walk.element( ) < small.element( ):
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__ (self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList( )

    def __len__ (self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min( )
        item = p.element( )
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min( )
        item = self._data.delete(p)
        return (item._key, item._value)