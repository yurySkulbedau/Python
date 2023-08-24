# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной.
#
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


def read_file(path, delimeter=','):
    """
    Чтение данных из файла и преобразование в список словарей.
    :param path: Путь к файлу.
    :param delimeter: Разделитель данных в файле.
    :return: Список словарей с контактами.
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            lines = [line.strip().split(delimeter) for line in file.readlines()]
        return [dict(zip(lines[0], contact)) for contact in lines]
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return []


def menu(app_status=True):
    """
    Отображение главного меню и обработка выбора пользователя.
    :param app_status: Статус приложения (работает/не работает).
    """
    while app_status:
        print('\nГлавное меню:',
              '1 - Просмотреть все контакты',
              '2 - Поиск по фамилии',
              '3 - Поиск по телефону',
              '4 - Добавить контакт',
              '5 - Изменить контакт',
              '6 - Удалить контакт',
              '0 - Выйти из приложения', sep='\n    ')
        user_choice = input('Выберите действие: ')
        match user_choice:
            case '1':
                show_tbl(phonebook)
            case '2':
                find_contact(phonebook, by='Фамилия')
            case '3':
                find_contact(phonebook, by='Телефон')
            case '4':
                add_row(phonebook)
                show_tbl(phonebook)
            case '5':
                change_row(phonebook)
            case '6':
                del_row(phonebook)
            case '0':
                app_status = False
                save_file(phonebook, file_path)
            case _:
                print("Недопустимый ввод. Пожалуйста, выберите действие из списка.")
                menu()


def show_tbl(table, show_id=False):
    """
    Вывод таблицы контактов на экран
    :param table: Список словарей с контактами.
    :param show_id: При наличии этого параметра будет добавлен столбец "id".
    """
    if not table:
        print("Нет данных для отображения.")
        return

    if show_id:
        for id, row in enumerate(table):
            table[id]['id'] = str(id)
        table[0]['id'] = 'id'

    # для комфортного отображения:
    max_width = {key: max(len(str(contact[key])) for contact in table) + 2 for key in table[0]}  # 2 - отступы
    border_length = sum(max_width.values()) + len(max_width) - 1
    print('_' * border_length)

    for id, row in enumerate(table):
        row = [str(elem).ljust(max_width[key]) for key, elem in row.items()]
        print(*row)
        if id == 0:
            print('-' * border_length)
    print('-' * border_length)

    if show_id:
        for id, row in enumerate(table):
            del table[id]['id']
    else:
        input('Нажмите Enter, чтобы вернуться в меню')


def input_data(prompt):
    while True:
        data = input(prompt)
        if data:
            return data
        print('Вы оставили пустым поле для ввода')


def find_contact(table, by):
    """
    Поиск контакта по фамилии или телефону.
    :param table: Список словарей с контактами.
    :param by: Критерий поиска ('Фамилия' или 'Телефон').
    """
    to_find = input_data(f'{by}: ').lower()
    success = False
    for record in table:
        if by == 'Телефон':
            record[by] = ''.join(filter(lambda x: x.isdigit(), record[by]))  # Удаляем все, кроме цифр
            to_find = ''.join(filter(lambda x: x.isdigit(), to_find))
            if not to_find:
                print("Некорректный телефонный номер.")
                return
        if to_find in record[by].lower():
            print(*record.values())
            success = True
    if not success:
        print("Поиск не дал результатов :(")
    input('\nНажмите Enter, чтобы вернуться в меню')


def add_row(table):
    """
    Добавление нового контакта в телефонную книгу.
    :param table: Список словарей с контактами.
    """
    data = {key: input_data(f'{key}: ') for key in table[0] if key != 'Комментарий'}
    data.update({'Комментарий': input('Комментарий (можете оставить это поле пустым): ')})
    table.append(data)


def choose_id(question: str, table):
    id = int(input(f'{question} (введите id)? '))
    while id not in range(1, len(table)):
        print("Ошибка: индекс выходит за пределы списка.")
        id = int(input(f'{question} (введите id)? '))
    return id


def change_row(table):
    show_tbl(table, show_id=True)
    chng_contact = choose_id('Чьи данные изменить', table)
    print('\t'.join(table[chng_contact].values()))

    print('Какие данные хотите изменить?')
    print('0 - Выход')
    for i, key in enumerate(table[chng_contact].keys(), start=1):
        print(f'{i} - {key}')
    chng_data = input('Можно выбрать несколько: ')
    if '0' in chng_data:
        print('Изменение данных отменено.')
        return

    for i, key in enumerate(table[chng_contact].keys(), start=1):
        if str(i) in chng_data:
            table[chng_contact][key] = input(f'{key}: ')


def del_row(table):
    show_tbl(table, show_id=True)
    del_id = choose_id('Кого удалить', table)
    contact_to_delete = table[del_id]
    print('Вы собираетесь удалить:')
    print('\t'.join(contact_to_delete.values()))
    confirmation = input('Вы уверены, что хотите удалить этот контакт?\n(Введите "флюгегехаймен" для отмены): ')
    if confirmation.lower() == "флюгегехаймен":
        print('Удаление отменено')
    else:
        print(f'Удален контакт: {table.pop(del_id)}')
    input('Нажмите Enter, чтобы вернуться в меню')


def save_file(table, path):
    choice = input('Сохранить изменения? (Введите "да" для сохранения или Enter для отмены) ')
    if choice.lower() == 'да':
        with open(path, 'w', encoding='UTF-8') as output:
            for row in table:
                line = ','.join(row.values())
                output.write(line + '\n')


file_path = 'contacts.txt'
phonebook = read_file(file_path)

menu()
