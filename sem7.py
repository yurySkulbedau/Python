# '''lambda'''
# def summa(a, b, c, d):
#     return a + b + c + d

# lambda a, b, c, d: a + b + c + d


# lst = list('1234sd567fgdj890fgh')

# '''filter() & map()'''
# lst = list(filter(lambda x: x.isdigit(), lst))
# lst = list(map(int, lst))
# lst = list(map(lambda x: (x+10)*2, lst))

# '''enumerate()'''
# for i in enumerate(lst):
#     print(i)
# for i in enumerate(lst, 5):
#     print(i)
# for i, item in enumerate(lst):
#     print(item)


# '''zip()'''
# nums = list('12345678')
# lets = list('qwerasdf')
# puncts = list('!@#$%')

# new_list = list(zip(nums, lets, puncts))
# print(*new_list)


'''У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз 
и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.'''

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(lambda x: x, values))

# print(transormed_values)



'''Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой 
имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины 
полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса. При решении задачи используйте списочные 
выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти 
и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна'''

# from math import pi
# from random import randint


# def find_farthest_orbit(list_of_orbits):
#     print(list_of_orbits)
#     planets = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     print(planets)
#     squares = list(map(lambda x: x[0] * x[1], planets))
#     planets = list(zip(planets, squares))
#     print(planets)
#     return max(planets, key=lambda x: x[1])[0]


# # def find_farthest_orbit(list_of_orbits):
# #     s = [pi * a * b for a, b in list_of_orbits if a != b]
# #     return list_of_orbits[s.index(max(s))]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit([(randint(1, 10), randint(1, 10)) for _ in range(10)]))



'''Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект 
и вычисляет его характеристику.'''

def same_by(characteristic, objects):
    res = set(map(characteristic, objects))
    return len(res) < 2


func = lambda x: x % 2 == 0
print(same_by(func, [0, 2, 71, 10]))

func = lambda x: x % 2 == 0
print(same_by(func, [1, 5, 77]))

print(same_by(len, ['sdfg', 'dfg', 'sdfg']))
