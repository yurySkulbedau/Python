'''Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно 
ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

from input_functions import *

a1 = float_input('Enter the first element of the arithmetic progression: ')
d = float_input('Enter the difference of the arithmetic progression: ')
N = integer_input('Enter the amount of numbers: ')

ar_prog = [(a1 + (n - 1) * d) for n in range(1, N + 1)]
print(ar_prog)
