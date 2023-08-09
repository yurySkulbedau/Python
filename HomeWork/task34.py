'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам'''

def is_there_rhythm(line):
    only_vowels = [list(filter(lambda x: x in vowels, word)) for word in line.split()]
    vowel_counts = set(map(len, only_vowels))
    if len(vowel_counts) > 1 or vowel_counts == {0}:
        return 'Пам парам'
    return 'Парам пам-пам'


vowels = 'уеёыаоэюия'

example_song = 'пара-ра-рам рам-пам-папам па-ра-па-да'
print('Example song: ', example_song)
print(is_there_rhythm(example_song), '\n')

song = input('Введите стихотворение Винни-Пуха (in Russian, please): ')
print(is_there_rhythm(song))
