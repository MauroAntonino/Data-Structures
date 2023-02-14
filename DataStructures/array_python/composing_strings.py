import time
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
list_of_strings = id_generator(3000)
b = ""

start = time.time()
for letters in list_of_strings:
    b += letters
end = time.time()
print(end - start)
time.sleep(5)

start = time.time()
temp = [ ] # start with empty list
for c in list_of_strings:
    temp.append(c) # append alphabetic character
letters = ''.join(temp)
end = time.time()
print(end - start)

time.sleep(5)
start = time.time()
letters = ''.join([c for c in list_of_strings])
end = time.time()
print(end - start)