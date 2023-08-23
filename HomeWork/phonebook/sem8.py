'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных'''

def read_file(path, delimeter=','):
    with open(path, 'r', encoding='UTF-8') as file:
        lines = [line.strip().split(delimeter) for line in file.readlines()]
    return lines


def input_data(prompt):
    while True:
        data = input(prompt)
        if data:
            return data
        print('Вы оставили пустым поле для ввода')


def show_tbl(table, show_id=False):
    max_width = [max(len(row[i]) for row in table) for i in range(len(table[0]))]  # для комфортного отображения
    print('_' * sum(max_width))
    for id, row in enumerate(table):
        row = [id] * show_id + [elem.ljust(max_width[j]) for j, elem in enumerate(row)]
        print(*row)
    print('-' * sum(max_width))
    if not show_id:
        input('Нажмите Enter, чтобы вернуться в меню')


def find_contact(table, by):
    book = [dict(zip(table[0], contact)) for contact in table[1:]]
    to_find = input_data(f'{by}: ').lower()
    success = False
    for record in book:
        if by == 'Телефон':
            record[by] = ''.join(filter(lambda x: x.isdigit(), record[by]))
        if to_find in record[by].lower():
            print(*record.values())
            success = True
    if not success:
        print("Поиск не дал результатов :(")
    input('Нажмите Enter, чтобы вернуться в меню')


def add_row(table):
    fields = ['Фамилия', 'Имя', 'Номер телефона']
    data = [input_data(f'{field}: ') for field in fields]
    data += [input('Комментарий: ')]
    table.append(data)


def del_row(table):
    show_tbl(table, show_id=True)
    del_contact = int(input('Кого удалить (введите id)? '))


def leave_app(table, path):
    answer = input('Сохранить изменения? (Введите "да" для сохранения) ')
    if answer == 'да':
        with open(path, 'w', encoding='UTF-8') as output:
            for row in table:
                line = ','.join(row)
                output.write(line + '\n')


file_path = 'HomeWork\phonebook\contacts.txt'
phonebook = read_file(file_path)
print(phonebook)

app_status = True
while app_status:
    user_choice = int(input('''\nВыберите действие:
    1 - Просмотреть все контакты
    2 - Поиск по фамилии
    3 - Поиск по телефону
    4 - Добавить контакт
    5 - Изменить контакт
    6 - Удалить контакт
    0 - Выйти из приложения\n'''))
    match user_choice:
        case 1:
            show_tbl(phonebook)
        case 2:
            find_contact(phonebook, by='Фамилия')
        case 3:
            find_contact(phonebook, by='Телефон')
        case 4:
            add_row(phonebook)
            show_tbl(phonebook)
        case 6:
            del_row(phonebook)
        case 0:
            app_status = False
            leave_app(phonebook, file_path)
