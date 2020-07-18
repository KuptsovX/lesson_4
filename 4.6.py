from itertools import count
from itertools import cycle
number = int(input('Введите число до которого вести счет: '))
my_list = []
for el in count(1):
    if el > number:
        break
    else:
        my_list.append(el)
cycle_list = cycle(my_list)
next(cycle_list)
new_list = []
for i in range(len(my_list)):
    next_element = next(cycle_list)
    new_list.append(next_element)
    new_list.sort()
print(my_list)
print(new_list)