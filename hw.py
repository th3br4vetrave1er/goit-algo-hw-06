class Field: # Базовый класс для полей записи
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Класс для хранения имени контакта Обязательно поле.
    pass

class Phone(Field): # Класс для хранения телефона. Имеет валидацию формата (10 цифр).
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_phone():
            raise ValueError("Invalid phone number format.")

    def validate_phone(self):
        return len(self.value) == 10 and self.value.isdigit() # Реализована валидация номера телефона (должна быть проверка на 10цифры).

class Record: # Класс хранения информации о контакте, включая имя и список телефонов.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
# Реализованы методы добавления - add_phone/удаления - remove_phone/редактирования - edit_phone/поиска объектов Phone- find_phone.
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return
        raise ValueError("Phone number not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError("Phone number not found.")

    def __str__(self):
        phone_numbers = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_numbers}"

class AddressBook: # Класс для хранения и управления записями.
    def __init__(self):
        self.data = {}

    def add_record(self, record): # Реализован метод add_record, добавляющий запись в self.data.
        self.data[record.name.value] = record # Класс Record: Реализовано хранение объекта Nameв отдельном атрибуте.

    def find(self, name): # Реализован метод find, находящий запись по имени.
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError("Contact not found.")

    def delete(self, name): # Реализован метод delete, удаляющий запись по имени.
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found.")
