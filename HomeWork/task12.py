'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
S = int(input("Enter sum: "))
P = int(input("Enter product: "))

found_solution = False

for x in range(1001):
    y = S - x
    if (x * y == P):
        found_solution = True
        print(f"The numbers he had in mind: {x} and {y}")
        break

if not found_solution:
    print("Incorrect values")