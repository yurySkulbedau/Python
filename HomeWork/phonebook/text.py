main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

input_choice = 'Выберите пункт меню: '
input_menu_error = f'Введенное число должно быть от 1 до {len(main_menu) - 1}'

file_load_successful = 'Телефонная книга успешно загружена!'

file_save_successful = 'Телефонная книга успешно сохранена!'

empty_phone_book = 'Телефонная книга пуста или не загружена'

new_contact = ['Введите имя: ', 'Введите телефон: ', 'Введите комментарий: ']

for_search = 'Введите ключевое слово для поиска: '

for_edit = 'Введите ключевое слово для поиска изменяемого контакта: '
input_edit_id = 'Введите ID изменяемого контакта: '
input_edit_contact = ['Введите новое имя (или нажмите Enter, чтобы оставить без изменений): ',
                      'Введите новый номер телефона (или нажмите Enter, чтобы оставить без изменений): ',
                      'Введите новый комментарий (или нажмите Enter, чтобы оставить без изменений): ']

for_delete = 'Введите ключевое слово для поиска удаляемого контакта: '
input_del_id = 'Введите ID удаляемого контакта: '

confirm_changes = 'Книга была изменена. Сохранить? (y/n)\n'
end_programm = 'До свидания! До новых встреч!'


def operation_with(name: str, operation: str):
    return f'Контакт {name} успешно {operation}!'


def not_found(word: str):
    return f'Контакты, содержащие "{word}" не найдены :('