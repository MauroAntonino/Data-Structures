class Node:
    def __init__(self, element, next=None): # initialize node’s fields
        __slots__ = 'element' , 'next' # streamline memory usage
        self.element = element # reference to user’s element
        self.next = next # reference to next node

class LinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail= None
    
    def __str__(self) -> str:
        lista = ["[ "]
        current = self.head
        while current != None:
            if current.next != None:
                lista.append(str(current.element))
                lista.append(", ")
            else: 
                lista.append(str(current.element))
            current = current.next
        lista.append(" ]")
        return "".join(lista)
    
    def push_front(self, e):
        newest = Node(e)
        newest.next = self.head
        self.head = newest
        if self.size == 0:
            self.tail = newest
        self.size = self.size + 1
    
    def pop_front(self):
        self.head = self.head.next
        if self.size == 1:
            self.tail = None
        self.size -= 1
    
    def push_back(self, e):
        newest = Node(e)
        newest.next = None
        if self.size == 0:
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size = self.size + 1
    
    def pop_back(self):
        if self.size == 0:
            self.tail = None
            self.head = None
            return None
        current = self.head
        while current != self.tail:
            if current.next == self.tail:
                self.tail = current
                current.next = None
                return current.element
            current = current.next
        if self.size == 0:
            self.tail = None
            self.head = None
            return None
        self.size -= 1
    
    def size_l(self):
        return self.size
    
    def empty(self):
        if self.size == 0:
            return True
        return False
    
    def value_at(self, index):
        cont = 0
        current = self.head
        while cont < index:
            current = current.next
            cont += 1
            if (current.next == None) and cont < index:
                raise IndexError("index not found")
        return current.element
    
    def front(self):
        return self.head.element
    
    def back(self):
        return self.tail.element
    
    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
            return
        if index == self.size - 1:
            self.push_back(value)
            return
        if self.size == 0:
            node.next = None
            self.head = node
            self.tail = node
            return
        node = Node(value)
        cont = 0
        current = self.head
        while cont < index:
            if cont == index - 1:
                node.next = current.next
                current.next = node
            current = current.next
            cont += 1
            if (current == None):
                raise IndexError("index not found")
        self.size += 1

# lista = LinkedList()
# lista.push_front("e")
# lista.push_front("b")
# print(lista)
# print(lista.empty())
# print(lista.value_at(0))
# try:
#     print(lista.value_at(5))
# except Exception as e: print(e)
# lista.pop_front()
# lista.pop_front()
# print(lista)
# lista.push_back(32)
# lista.push_back(26)
# lista.push_front(3)
# print(lista)
# print(lista.head.element)
# lista.pop_back()
# print(lista)
# print(lista.tail.element)
# print(lista.front())
# print(lista.back())
# lista.insert(0, 59)
# lista.insert(1, 81)
# lista.insert(4, 152)
# lista.insert(4, 16)
# print(lista)
# print(lista.tail.element)
# try:
#     lista.insert(78, 16)
# except Exception as e: print(e)