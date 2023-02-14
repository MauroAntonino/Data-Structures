import time
import random
import string
from DataStructures.array_python.array import DynamicArray
from DataStructures.linked_lists.linked_lists import LinkedList
from python_datastructures import SinglyLinkedList

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
NUMBER = 10000
list_of_strings = id_generator(NUMBER)
b = ""

class Testing:
    def __init__(self) -> None:
        self.lst_py = None
        self.lst_da = None
        self.lst_ll = None
        self.lst_li = None
        self.append()
        self.insert()
        self.remove()
        
    def append(self):
        print("append")
        start = time.time()
        temp = [] # start with empty list
        for c in list_of_strings:
            temp.append(c) # append alphabetic character
        end = time.time()
        self.lst_py = temp
        print("lista de python: ", end - start)

        start = time.time()
        temp = DynamicArray() # start with empty list
        for c in list_of_strings:
            temp.push(c) # append alphabetic character
        end = time.time()
        self.lst_da = temp
        print("lista implementada: ", end - start)

        start = time.time()
        temp = LinkedList() # start with empty list
        for c in list_of_strings:
            temp.push_back(c) # append alphabetic character
        end = time.time()
        self.lst_ll = temp
        print("linked list implementada: ", end - start)

        start = time.time()
        temp = SinglyLinkedList() # start with empty list
        for c in list_of_strings:
            temp.add(c) # append alphabetic character
        end = time.time()
        self.lst_li = temp
        print("linked list importada: ", end - start)

    def insert(self):
        print("insert")
        start = time.time()
        for c in range(1000):
            self.lst_py.insert(NUMBER//2, c) # append alphabetic character
        end = time.time()
        print("lista de python: ", end - start)

        start = time.time()
        for c in range(1000):
            self.lst_da.insert(NUMBER//2, c) # append alphabetic character
        end = time.time()
        print("lista implementada: ", end - start)

        start = time.time()
        for c in range(1000):
            self.lst_ll.insert(NUMBER//2, c) # append alphabetic character
        end = time.time()
        print("linked list implementada: ", end - start)

        for c in range(1000):
            self.lst_li.add(c)
        print("linked list importada: ", "não possui")
    
    def remove(self):
        print("remove")
        start = time.time()
        for c in range(1000):
            self.lst_py.remove(c) # append alphabetic character
        end = time.time()
        print("lista de python: ", end - start)

        start = time.time()
        for c in range(1000):
            self.lst_da.remove(c) # append alphabetic character
        end = time.time()
        print("lista implementada: ", end - start)

        # start = time.time()
        # for c in range(1000):
        #     self.lst_ll.insert(NUMBER//2, c) # append alphabetic character
        # end = time.time()
        # print("linked list implementada: ", end - start)

        # for c in range(1000):
        #     self.lst_li.add(c)
        # print("linked list importada: ", "não possui")

Testing()