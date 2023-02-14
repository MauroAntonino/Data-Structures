class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __str__(self):
        return str(self._data[self._front: self._front + self._size])

    def len(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty( ):
            raise Exception('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty( ):
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """
        Add an element to the back of queue.
        """
        if self._size == len(self._data):
            self.resize(2*len(self._data)) # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap): # we assume cap >= len(self)
        """
        Resize to a new list of capacity >= len(self).
        """
        old = self._data # keep track of existing list
        self._data = [None]*cap # allocate list with new capacity
        walk = self._front
        for k in range(self._size): # only consider existing elements
            self._data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
        self._front = 0

# queue = ArrayQueue()
# queue.enqueue(10)
# queue.enqueue(21)
# queue.enqueue(47)
# queue.enqueue(686)
# queue.enqueue(325)
# queue.enqueue(90)
# queue.enqueue(24)
# queue.enqueue(74)
# queue.enqueue(29)
# queue.enqueue(33)
# queue.enqueue(97)
# queue.enqueue(178)
# print(queue)
# queue.dequeue()
# queue.dequeue()
# print(queue)
