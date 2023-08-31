from copy import deepcopy

PATH = 'phones.txt'

phonebook = {}
original_book = {}


def open_file(delimeter=','):
    global phonebook, original_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data, start=1):
        contact = contact.strip().split(delimeter)
        phonebook[i] = contact
    original_book = deepcopy(phonebook)


def save_file(delimeter=','):
    global phonebook
    data = [delimeter.join(contact) for contact in phonebook.values()]
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def add_contact(new: list[str]):
    global phonebook
    c_id = max(phonebook) + 1
    phonebook[c_id] = new


def search(word: str) -> dict[int, list[str]]:
    global phonebook
    result = {}
    for i, contact in phonebook.items():
        for field in contact:
            if word.lower() in field.lower():
                result[i] = contact
                break
    return result


# def check_chosen_id(c_id: int, book: dict):
#     return c_id in book


def edit(c_id: int, contact: list[str]) -> str:
    global phonebook
    current_contact = phonebook.get(c_id)
    corr_contact = [contact[i] if contact[i] else current_contact[i] for i in range(3)]
    phonebook[c_id] = corr_contact
    return corr_contact[0]


def del_contact(c_id: int) -> list[str]:
    global phonebook
    return phonebook.pop(c_id)