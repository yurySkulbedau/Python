'''Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве.'''

from random import randint

# N = 12
# M = 6

# first_arr = [randint(0, 10) for _ in range(N)]
# print(*first_arr)
# second_arr = [randint(0, 10) for _ in range(M)]
# print(*second_arr)

# print([elem for elem in first_arr if elem not in second_arr])


'''Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного.'''

# N = 12
# arr = [randint(0, 10) for _ in range(N)]
# print(*arr)

# res_arr = [arr[i] for i in range(1, len(arr) - 1) if arr[i-1] < arr[i] > arr[i+1]]
# print(res_arr)
# print(len(res_arr))


'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.'''

# N = 20
# arr = [randint(0, 10) for _ in range(N)]
# print(*arr)
# # arr = sorted(arr)
# # print(*arr)

# count = 0
# for elem in set(arr):
#     count += arr.count(elem) // 2
# print(count)
# # print(sum([arr.count(item)//2 for item in set(arr)]))


'''Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) 
равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, 
разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).'''

def find_sum_divisors(n):
    divisors = [num for num in range(1, n // 2 + 1) if n % num == 0]
    return sum(divisors)


# arr = [{i, find_sum_divisors(i)} for i in range(10000) if find_sum_divisors(find_sum_divisors(i)) == i]

# for item in arr:
#     if arr.count(item) > 1:
#         arr.remove(item)
#     if len(item) == 2:
#         print(*item)

# адаптированное решение с семинара:

sum_dict = {i: find_sum_divisors(i) for i in range(10000)}
for key, value in sum_dict.items():
    if key == sum_dict.get(value) and key < value:
        print(key, value)
