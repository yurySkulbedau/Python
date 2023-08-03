'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint

N = 10
arr = [randint(0, 10) for _ in range(N)]
print(*arr)

min_range = int(input('Enter the minimum of the range: '))
max_range = int(input('Enter the maximum of the range: '))
if min_range > max_range:
    print("Most likely, you've made a mistake. All right, I'll correct your range.")
    min_range, max_range = max_range, min_range

indices = [i for i in range(N) if min_range <= arr[i] <= max_range]
print('Indices of elements belonging to the given range:', indices)
