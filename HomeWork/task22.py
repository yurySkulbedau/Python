'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

from random import randint


def get_random_set():
    num_elements = int(input("Enter number of elements in the set: "))
    random_list = [randint(-1, 9) for _ in range(num_elements)]
    print(random_list)
    return set(random_list)


first_set = get_random_set()
second_set = get_random_set()

intersection_set = first_set.intersection(second_set)

sorted_intersection = sorted(intersection_set)

print("\nNumbers that occur in both sets:", end=' ')
for num in sorted_intersection:
    print(num, end=' ')
