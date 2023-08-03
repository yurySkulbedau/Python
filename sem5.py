# Урок 5. Рекурсия и алгоритмы
'''Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи'''

# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n-1) + fib(n-2)


# N = int(input("N = "))
# print(fib(N))


'''Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.'''

from random import randint


# def change_grade(lst):
#     mini = min(lst)
#     maxi = max(lst)
#     return [mini if grade == maxi else grade for grade in lst]

# max_grade = 5
# min_grade = 2
# grade_list = [randint(min_grade, max_grade) for _ in range(10)]
# print(grade_list)
# antihacked_list = change_grade(grade_list)
# print(*antihacked_list)


''' Напишите функцию, которая принимает одно число и проверяет, является ли оно простым'''
# N = int(input('Enter the number: '))

# def isPrime(n):
#     if n % 2 == 0:
#         return False
#     for dev in range(3, int(n**0.5) + 1, 2):
#         if n % dev == 0:
#             return False
#     return True

# answer = 'простое' if isPrime(N) else 'составное'
# print(f"{N} - {answer}")


'''Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).'''

N = int(input("How many numbers? "))

def reverse(n):
    if n == 0:
        return
    number = int(input('Enter a number: '))
    reverse(n-1)
    print(number, end = ' ')

reverse(N)