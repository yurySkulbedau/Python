'''1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]'''

# lst = [1, 2, 3, 5, 8, 15, 23, 38]

# new = [(a, a*a) for a in lst if a % 2 == 0]
# print(new)


def select(f, col):  ### по сути - это функция map()
    return [f(x) for x in col]
'''Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.'''


def where(f, col):  ### по сути - это функция filter()
    return [x for x in col if f(x)]
'''Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для которых функция вернула True.'''


data = [1, 2, 3.0, 5, 8, 15, 23, 38]
# data = list(map(int, input().split()))

res = select(int, data)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]

res = select(lambda x: (x, x ** 2), res)
print(res)
print()


'''Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
из элементов входных данных'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# Функция zip () пробегает по минимальному входящему набору:
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
