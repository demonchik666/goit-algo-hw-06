from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    #додавання валідації для номера телефону
    def __init__(self, value):
        counter = 0
        for symbol in value:
            if symbol.isdigit():
                counter += 1
        if counter != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    #Додавання номера телефону до запису
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    #Зміна номера телефону з валідацією
    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                try:
                    self.phones[i] = Phone(new_phone)
                except ValueError as e:
                    print(e)
                return
        print("Phone number not found.")

    #Пошук номера телефону в записі
    def find_phone(self, phone):
        for given_phone in self.phones:
            if given_phone.value == phone:
                return given_phone.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу адресної книги
    def add_record(self, record):
        self.data[record.name.value] = record

    # Додавання запису до адресної книги
    def find(self, name) -> Record:
        return self.data.get(name, None)
    
    # Пошук запису за ім'ям
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        records = [str(record) for record in self.data.values()]
        return "\n".join(records) if records else "Address book is empty."

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
