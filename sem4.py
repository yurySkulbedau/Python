'''Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.'''

# мое решение
# str = '1324584512154654684846543242487'
# lst = list(str)
# res_list = [0] * len(lst)
# for i in range(len(lst)):
#     res_list[i] = f'{lst[i]}_{lst[:i].count(lst[i])}' if lst[:i].count(lst[i]) else lst[i]

# # улучшенное с помощью ChatGPT:
# def count_duplicates(string):
#     result_list = []
#     count_dict = {}
    
#     for char in string:
#         if char not in count_dict:
#             count_dict[char] = 0
#             result_list.append(char)
#         else:
#             count_dict[char] += 1
#             result_list.append(f'{char}_{count_dict[char]}')
    
#     return result_list

# input_str = '1324584512154654684846543242487'
# res_list = count_duplicates(input_str)
# print(res_list)


# # лучшее решение с семинара
# some_string = input("Введите строку: ")
# cnt_dict = {}
# for ch in some_string:
#     cnt_dict[ch] = cnt_dict.get(ch, -1) + 1 # если первый раз встречается, то метод .get положит этому ключу -1, сразу прибавится 1, итого: 0
#     print(ch if cnt_dict[ch] < 1 else f'{ch}_{cnt_dict[ch]}', end=' ')


# '''Пользователь вводит текст(строка). Слова разделены одним 
# или большим числом пробелов или символами конца строки. Определите, сколько различных слов содержится в этом тексте.'''

# from string import punctuation

# #print(punctuation)
# for char in punctuation:
#     text = text.replace(char, ' ')
# print(len(set(text.lower().split())))


'''Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)'''

import random

n = 50
sequence = [random.randint(0, 10) for _ in range(n)]
print(*sequence)

for i, elem in enumerate(sequence):
    if elem == 0:
        res_seq = sequence[:i]
        break
print(max(res_seq))


