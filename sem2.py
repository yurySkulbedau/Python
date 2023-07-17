# 9.
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120

# n = int(input("Enter positive integer: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print(f"{n}! = {fact}")


# 11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

# n = int(input("Enter positive integer: "))
# previous = 0
# fib_num = 1
# i = 2

# while fib_num < n:
#     previous, fib_num = fib_num, fib_num + previous
#     i += 1
# if fib_num == n:
#     print(i)
# else:
#     print(-1)


# 13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за 
# погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько
# дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10 Output: 2

import random

days = int(input())
count = 0
record = 0
for i in range(days):
    temp = random.randint(-50, 50)
    print(temp)
    if temp > 0:
        count += 1
    else:
        if count > record:
            record = count
        count = 0
print(f"подряд {record}")

