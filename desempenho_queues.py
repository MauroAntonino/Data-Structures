from collections import deque
import time
import random
import string
from DataStructures.queue.queue import ArrayQueue
from DataStructures.queue.linked_queue import LinkedQueue
# from python_datastructures import SinglyLinkedList

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
NUMBER = 1000000
list_of_strings = id_generator(NUMBER)
b = ""

class Testing:
    def __init__(self) -> None:
        self.que_py = None
        self.lst_da = None
        self.lst_ll = None
        self.que_qi = None
        self.append()
        
    def append(self):
        print("append")
        start = time.time()
        temp = ArrayQueue()
        for c in list_of_strings:
            temp.enqueue(c) # append alphabetic character
        end = time.time()
        self.que_qi = temp
        print("queue implementada: ", end - start)

        start = time.time()
        temp = LinkedQueue()
        for c in list_of_strings:
            temp.enqueue(c) # append alphabetic character
        end = time.time()
        self.que_qi = temp
        print("queue de linked implementada: ", end - start)

        start = time.time()
        temp = deque() # start with empty list
        for c in list_of_strings:
            temp.append(c) # append alphabetic character
        end = time.time()
        self.que_py = temp
        print("queue de python: ", end - start)

        start = time.time()
        temp = [] # start with empty list
        for c in list_of_strings:
            temp.append(c) # append alphabetic character
        end = time.time()
        self.que_py = temp
        print("lista de python: ", end - start)

Testing()