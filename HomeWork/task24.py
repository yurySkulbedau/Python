'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
некоторым кустом заданной во входном файле грядки.'''

from random import randint


def get_berry_picking(lst, bush_number, bushes_in_a_row=3):
    shifted_list = lst[bush_number:] + lst[:bush_number]
    return sum(shifted_list[:bushes_in_a_row])


num_bushes = int(input("Enter number of bushes: "))
num_berries = [randint(1,20) for _ in range(num_bushes)]
print("berries on each bush: ", *num_berries)

berry_pick = [get_berry_picking(num_berries, i) for i in range(num_bushes)]
print("the maximum number of berries that can be picked in one go", max(berry_pick))
