class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        slots = '_key' , '_value'

        def __init__ (self, k, v):
            self._key = k
            self._value = v

        def __lt__ (self, other):
            return self._key < other._key # compare items based on their keys

    def is_empty(self): # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0