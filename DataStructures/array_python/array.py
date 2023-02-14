import ctypes # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__ (self):
        """Create an empty array."""
        self.n = 0 # count actual elements
        self.capacity = 1 # default array capacity
        self.A = self. makearray(self.capacity) # low-level array

    def __len__ (self):
        """Return number of elements stored in the array."""
        return self.n

    def __getitem__ (self, k):
        """Return element at index k."""
        if not 0 <= k < self.n:
            raise IndexError( "invalid index" )
        return self.A[k] # retrieve from array
    
    def __str__(self) -> str:
        lst = ""
        lst += "[ "
        n = 1
        for item in self.A:
            if self.n == n:
                lst += item
                break
            item = item + ", "
            lst += item
            n += 1
        lst += " ]"
        return lst


    def push(self, obj):
        """Add object to end of the array."""
        if self.n == self.capacity: # not enough room
            self.resize(2*self.capacity) # so double capacity
        self.A[self.n] = obj
        self.n += 1

    def resize(self, c): # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self.makearray(c) # new (bigger) array
        for k in range(self.n): # for each existing value
            B[k] = self.A[k]
        self.A = B # use the bigger array
        self.capacity = c
    
    def size(self):
        return self.n
    
    def at(self, index):
        return self.A[index]
    
    def insert(self, index, item):
        if self.n == self.capacity: # not enough room
            self.resize(2*self.capacity) # so double capacity
        for element in range(self.n, index, -1):
            self.A[element] = self.A[element - 1]
        self.A[index] = item
        self.n += 1
    
    def prepend(self, index):
        self.insert(0, index)
        return
    
    def pop(self):
        response = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return response

    def delete(self, index):
        self.A[index] = None
        for element in range(index, self.n):
            self.A[element] = self.A[element + 1]
        self.n -= 1
    
    def shift_back(self, arr, pos_0, pos_1):
        arr[pos_0] = arr[pos_1]
        return arr
        
    def remove(self, item):
        start = 0
        end = 0
        while start < self.n:
            try:
                while self.A[end] == item:
                    end += 1    
            except: pass
            if start != end:
                try:
                    self.A = self.shift_back(self.A, start, end)
                except: pass
            start += 1
            end += 1
        self.n = self.n - (end - start)
        return
    
    def find(self, item):
        cont = 0
        while cont < self.n:
            if self.A[cont] == item:
                return cont
            cont += 1
        return -1

    def capacity_arr(self):
        return self.capacity
    
    def is_empty(self):
        if self.n == 0:
            return True
        return False

    def makearray(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c*ctypes.py_object)( )

# arr = DynamicArray()
# arr.push("21")
# arr.push("7")
# print(arr.is_empty())
# print(arr.at(1))
# arr.push("12")
# arr.insert(1, "19")
# arr.prepend("3")
# arr.pop()
# print(arr)
# arr.delete(3)
# print(arr)
# arr.push("21")
# arr.push("19")
# arr.push("57")
# arr.push("21")
# arr.push("21")
# print(arr)
# arr.remove("21")
# print(arr)
# print(arr.find("21"))
# print(arr.find("19"))