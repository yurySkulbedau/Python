import model
import view
import text


def search_block(msg: str):
    request = view.input_request(msg)
    result = model.search(request)
    view.show_book(result, text.not_found(request))
    if result:
        return True


def start():
    while True: 
        choice = view.menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.file_load_successful)
            case 2:
                model.save_file()
                view.print_message(text.file_save_successful)
            case 3:
                view.show_book(model.phonebook, text.empty_phone_book)
            case 4:
                contact = view.input_contact(text.new_contact)
                model.add_contact(contact)
                view.print_message(text.operation_with(contact[0], 'сохранен'))
            case 5:
                search_block(text.for_search)
            case 6:
                # # book = model.phonebook
                # # view.show_book(book, text.empty_phone_book)
                # result = {}
                if search_block(text.for_edit):
                # print(result)
                # while True:
                #     edit_id = int(view.input_request(text.input_edit_id))
                #     if model.check_chosen_id(edit_id, result):
                #         break
                    edit_id = int(view.input_request(text.input_edit_id))
                    corr_contact = view.input_contact(text.input_edit_contact)
                    name = model.edit(edit_id, corr_contact)
                    view.print_message(text.operation_with(name, 'изменен'))
            case 7:
                if search_block(text.for_delete):
                    del_id = int(view.input_request(text.input_del_id))
                    name = model.del_contact(del_id)[0]
                    view.print_message(text.operation_with(name, 'удален'))
            case 8:
                if model.phonebook != model.original_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        model.save_file()
                        view.print_message(text.file_save_successful)
                view.print_message(text.end_programm)
                break
