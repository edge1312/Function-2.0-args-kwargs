import json

class Contact:

    def __init__(self, first_name, last_name, phone_number, fav=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.fav = fav
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        res_1 = f'Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone_number}\nВ избранных: '
        res_fav = lambda x: "да" if self.fav==True else "нет"
        res_2 = f'{res_fav(self.fav)}\n'
        if not self.args and not self.kwargs:
            result = res_1 + res_2
        else:
            res_3 = 'Дополнительная информация:\n'
            args_data = ''.rjust(9)
            for data in self.args:
                args_data = args_data.rjust(9) + str(data) + '\n' + ''.rjust(9)
            kwargs_data = ''
            for data in self.kwargs:
                kwargs_data = kwargs_data + str(data)+ ' : ' + str(self.kwargs.get(data)) + '\n' + ''.rjust(9)
            result = res_1 + res_2 + res_3 + args_data + kwargs_data
        return result


class PhoneBook(object):

    def __init__(self, book_name):
        self.book_name = book_name
        self.contacts = {}

    def print_contacts(self):
        print('Список контактов:\n')
        for contact in self.contacts:
            print(f'"{contact}"\n{self.contacts.get(contact)}')

    def add_contact(self, first_name, last_name, phone_number, fav=False, *args, **kwargs):
        new_contact = {}
        new_contact[first_name + last_name] = Contact(first_name, last_name, phone_number, fav, args, kwargs)
        if first_name + last_name in self.contacts.keys():
            print('Такой контакт уже существует')
            check_input = ''
            while check_input not in ['y', 'Y', 'n', 'N']:
                check_input = input('Заменить его? (Y/N): ')
            if check_input in ['y', 'Y']:
                self.contacts.update(new_contact)
        else:
            self.contacts.update(new_contact)

        file_name = self.book_name + '.json'
        with open(file_name, 'w', encoding='utf-8') as file:
            data = {}
            for contact in self.contacts:
                data.update({contact:(self.contacts.get(contact).first_name,
                                      self.contacts.get(contact).last_name,
                                      self.contacts.get(contact).phone_number,
                                      self.contacts.get(contact).fav,
                                      self.contacts.get(contact).args,
                                      self.contacts.get(contact).kwargs
                                      )})
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_contact(self, phone_number):
        self.phone_number = phone_number
        print(self.phone_number)
        for contact in self.contacts:
            if self.contacts.get(contact).phone_number == self.phone_number:
                self.contacts.pop(contact)
                break

    def print_fav_numbers(self):
        for contact in self.contacts:
            if self.contacts.get(contact).fav == True:
                print(self.contacts.get(contact).phone_number)

    def search_contact(self, first_name, last_name):
        if first_name + last_name not in self.contacts.keys():
            print('Контакт не найден')
        else:
            print(self.contacts.get(first_name + last_name))




if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    vasya = Contact('Вася', 'Пупкин', '+74954959595', True, 'ООО "Рога и Копыта"', vk='id1133', mob_1='+79012345678')

    # print(jhon)
    # print(vasya)


    phone_book = PhoneBook('my_phone_book')
    phone_book.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    phone_book.add_contact('Jane', 'Smith', '+71234567810', telegram='@janny', email='janny@smith.com')
    # phone_book.add_contact('Jhon', 'Smith', '+71234567811', telegram='@jhony', email='jhony@smith.com')
    phone_book.add_contact('Вася', 'Пупкин', '+74957777777', True, 'ООО "Рога и Копыта"', vk='id1133')


    # print(phone_book.contacts.get('Jane'+'Smith'))

    # print(jhon)

    # print(phone_book.contacts)
    # print(type(phone_book.contacts))
    #
    # phone_book.search_contact('Jhon', 'Smith')
    #
    # phone_book.print_contacts()

    # phone_book.delete_contact('+71234567810')
    #
    # phone_book.print_contacts()

    #phone_book.print_fav_numbers()