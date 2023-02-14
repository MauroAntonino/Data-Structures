from DataStructures.queue.linked_queue import LinkedQueue

def preorder(self):
    """Generate a preorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_preorder(self.root()): # start recursion
            yield p

def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    yield p # visit p before its subtrees
    for c in self.children(p): # for each child c
        for other in self._subtree_preorder(c): # do preorder of c’s subtree
            yield other # yielding each to our caller


def postorder(self):
    """Generate a postorder iteration of positions in the tree."""
    if not self.is_empty( ):
        for p in self._subtree_postorder(self.root( )): # start recursion
            yield p

def _subtree_postorder(self, p):
    """Generate a postorder iteration of positions in subtree rooted at p."""
    for c in self.children(p): # for each child c
        for other in self._subtree_postorder(c): # do postorder of c’s subtree
            yield other # yielding each to our caller
    yield p
    

def breadthfirst(self):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not self.is_empty( ):
        fringe = LinkedQueue( ) # known positions not yet yielded
        fringe.enqueue(self.root( )) # starting with the root
        while not fringe.is_empty( ):
            p = fringe.dequeue( ) # remove from front of the queue
            yield p # report this position
            for c in self.children(p):
                fringe.enqueue(c) # add children to back of queue