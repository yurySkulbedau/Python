''' 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть
'''
import random

n = int(input("Enter number of coins: "))
heads = 0
tails = 0
coins = []  # массив исключительно для вывода информации о положениях монет
for i in range(n):
    pos = 'H' if random.randint(0, 1) == 0 else 'T'
    if pos == 'H':
        heads += 1
    else:
        tails += 1
    coins.append(pos)
print(*coins)
print(f"number of heads: {heads}")
print(f"number of tails: {tails}")
answer = heads if heads < tails else tails
print(f"Answer: {answer}")
