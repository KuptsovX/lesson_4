from itertools import count
from math import factorial

def my_func():
    for el in count(1):
        yield factorial(el)

x = 0
for i in my_func():
    if x < 15:
        print(i)
        x += 1
    else:
        break