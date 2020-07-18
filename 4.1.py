from sys import argv
name,time,salary,bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    result = (time * salary) + bonus
    print(f'Зарплата сотрудника {result} рублей')
except ValueError:
    print('Это не число')

