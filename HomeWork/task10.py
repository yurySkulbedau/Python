''' 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
которые нужно перевернуть
'''
from random import randint

n = int(input("Enter number of coins: "))
heads = 0
for _ in range(n):
    pos = 'H' if randint(0, 1) == 0 else 'T'
    if pos == 'H':
        heads += 1
    print(pos, end=' ')
print(f"\nnumber of heads: {heads}")
tails = n - heads
print(f"number of tails: {tails}")
answer = heads if heads < tails else tails
print(f"Answer: {answer}")
