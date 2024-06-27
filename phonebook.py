def initialize_phonebook(filename):
    initial_data = [
        "Иванов, Иван, 89012345601, Программист",
        "Петров, Петр, 89012345602, Врач",
        "Сидоров, Сидор, 89012345603, Учитель",
        "Смирнова, Мария, 89012345604, Бухгалтер",
        "Кузнецов, Алексей, 89012345605, Инженер",
        "Попова, Анна, 89012345606, Маркетолог",
        "Васильев, Дмитрий, 89012345607, Юрист",
        "Соколова, Елена, 89012345608, Дизайнер",
        "Морозов, Михаил, 89012345609, Менеджер",
        "Новикова, Ольга, 89012345610, Аналитик"
    ]
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in initial_data:
            phout.write(f'{record}\n')

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            result = find_by_lastname(phone_book, last_name)
            if result:
                print(result)
            else:
                print("Абонент не найден")
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            result = change_number(phone_book, last_name, new_number)
            print(result)
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            result = delete_by_lastname(phone_book, last_name)
            print(result)
        elif choice == 5:
            number = input('Введите номер: ')
            result = find_by_number(phone_book, number)
            if result:
                print(result)
            else:
                print("Абонент не найден")
        elif choice == 6:
            user_data = input('Введите новые данные (Фамилия, Имя, Номер, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
            print("Абонент добавлен.")
        elif choice == 7:
            source_file = input('Введите имя исходного файла: ')
            target_file = input('Введите имя целевого файла: ')
            row_number = int(input('Введите номер строки для копирования: '))
            copy_data(source_file, target_file, row_number)
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер телефона абонента\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Копировать данные из одного файла в другой\n"
          "8. Закончить работу")
    choice = int(input("Ваш выбор: "))
    return choice

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for record in phone_book:
        print(f"{record['Фамилия']}, {record['Имя']}, {record['Телефон']}, {record['Описание']}")

def find_by_lastname(phone_book, last_name):
    results = [record for record in phone_book if record['Фамилия'] == last_name]
    return results

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return "Номер изменен"
    return "Абонент не найден"

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return "Абонент удален"
    return "Абонент не найден"

def find_by_number(phone_book, number):
    for record in phone_book:
        if record['Телефон'] == number:
            return record
    return None

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_record = dict(zip(fields, user_data.split(',')))
    phone_book.append(new_record)

def copy_data(source_file, target_file, row_number):
    try:
        with open(source_file, 'r', encoding='utf-8') as src, open(target_file, 'a', encoding='utf-8') as tgt:
            lines = src.readlines()
            if 0 < row_number <= len(lines):
                tgt.write(lines[row_number - 1])
                print("Данные успешно скопированы.")
            else:
                print("Неверный номер строки.")
    except FileNotFoundError:
        print("Файл не найден.")

# Инициализация телефонной книги
initialize_phonebook('phon.txt')

# Запуск основной функции
work_with_phonebook()
