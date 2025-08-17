# задание 1
import os

import platform

import shutil


def main():
    # 1. Вывести имя  ОС
    os_name = platform.system()
    print(f"Имя вашей ОС: {os_name}")

    # 2. Вывести путь до текущей папки
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")

    # 3. Рассортировать файлы по расширениям

    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

    # Создать словарь расширений и соответствующих папок
    ext_dirs = {}
    for filename in files:
        ext = os.path.splitext(filename)[1].lower()
        if ext:
            dir_name = ext[1:]  # убрать точку
        else:
            dir_name = 'без_расширения'
        ext_dirs.setdefault(dir_name, []).append(filename)

    # Для каждого расширения создать папку и переместить файлы
    for ext, filenames in ext_dirs.items():
        target_dir = os.path.join(current_dir, ext)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for filename in filenames:
            src_path = os.path.join(current_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            shutil.move(src_path, dst_path)

            # 4.  Выводим сообщение о количестве и размере файлов
        total_size_bytes = sum(os.path.getsize(os.path.join(target_dir, f)) for f in filenames)
        total_size_gb = total_size_bytes / (1024 ** 3)  # перевод в гигабайты

        print(f"В папке с {ext} файлами перемещено {len(filenames)} файлов, их размер – {total_size_gb:.2f} ГБ.")

        # 5. Переименовать один файл в каждой поддиректории (если они есть)
        if filenames:
            old_name = filenames[0]
            old_path = os.path.join(target_dir, old_name)
            new_name = 'some_' + old_name
            new_path = os.path.join(target_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Файл {old_name} был переименован в {new_name}")


if __name__ == "__main__":
    main()

# задание 2

import os

os.mkdir("test9")

import re


def replace_defendant_name(text):
    # Шаблон для фамилии
    surname_pattern = r'[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?'
    # Имя и отчество
    name_pattern = r'[А-ЯЁ][а-яё]+'

    # Полный шаблон для поиска ФИО
    fio_pattern = rf'({surname_pattern})\s+({name_pattern})\s+({name_pattern})'

    def replacer(match):
        return 'N'

        # Замена

    new_text = re.sub(fio_pattern, replacer, text, count=1)

    return new_text

    #  текст


text = """Подсудимая Эверт-Колокольцева Елизавета Александровна
в судебном заседании... """

# результат
result = replace_defendant_name(text)
print(result)

# задание 3

import collections


def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, \
            open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()

            if line.lower() == 'стоп':
                break

            if not line:
                continue
                # разбиваем строку на слова
            words = line.split()
            # считаем частоту слов
            counter = collections.Counter(words)
            # находим самое часто встречающееся слово и количество
            most_common_word, count = counter.most_common(1)[0]
            # вывод
            outfile.write(f"{most_common_word} {count}\n")


input_file = input("Введите имя входного файла: ")
output_file = input("Введите имя выходного файла: ")

print("Введите строки текста. Для завершения введите 'стоп'.")
process_file(input_file, output_file)

# задание 4

import os

import re


def load_stop_words(filename):
    # Загружает список запрещённых слов из файла
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        # Разделяем слова по пробелам
        stop_words = content.strip().split()
        # Приводим все слова к нижнему регистру для сравнения
        stop_words = [word.lower() for word in stop_words]
    return stop_words


def censor_text(input_filename, stop_words):
    # Заменяет запрещённые слова в тексте на звездочки.
    with open(input_filename, 'r', encoding='utf-8') as f:
        text = f.read()

        # Создаём регулярное выражение для поиска всех слов
    # \b - граница слова, чтобы искать слова целиком
    pattern = re.compile(r'\b\w+\b', re.UNICODE)

    def replace_match(match):
        word = match.group()
        # Проверяем слово без учёта регистра
        if word.lower() in stop_words:
            return '*' * len(word)
        else:
            return word

            # Заменяем все запрещённые слова

    censored_text = pattern.sub(replace_match, text)
    return censored_text


def main():
    filename = input("Введите название файла для проверки: ")
    stop_words_file = 'stop_words.txt'

    stop_words = load_stop_words(stop_words_file)
    censored_content = censor_text(filename, stop_words)

    print("\nРезультат:\n")
    print(censored_content)


if __name__ == "__main__":
    main()

# задание 5

with open('main5', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 3:
            surname, name, grade_str = parts
            grade = int(grade_str)

            if grade < 3:
                print(f"{surname} {name} - {grade}")

# задание 6

import re

total_sum = 0
# открываем файл .txt
with open('hello_some.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        total_sum += sum(int(num) for num in numbers)

print(total_sum)

# задание 7

# Открываем файл .txt
with open('some.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    # Обрабатываем  строки
encrypted_lines = []
for i, line in enumerate(lines, start=1):
    line = line.rstrip('\n')  # Удаляем символ переноса строки
    encrypted_line = ''
    for char in line:
        if char.isalpha():
            # Определяем заглавные и строчные буквы
            base = ord('A') if char.isupper() else ord('a')
            # Символ с учетом шага
            shifted_char = chr((ord(char) - base + i) % 26 + base)
            encrypted_line += shifted_char
        else:
            # Если символ не буква, оставляем без изменений
            encrypted_line += char
    encrypted_lines.append(encrypted_line)

    # Вывод
for line in encrypted_lines:
    print(line)

# задание 8

import json
import csv
import os

# Путь к файлу JSON
JSON_FILE = 'employees.json'
# Путь к файлу CSV
CSV_FILE = 'employees.csv'


def load_json():
    # Загружает данные из JSON файла
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            return []


def save_json(data):
    # Сохраняет данные в JSON файл
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_to_csv():
    # Преобразует JSON в CSV
    data = load_json()
    if not data:
        print("Нет данных для преобразования.")
        return
    # Определяем заголовки
    headers = data[0].keys()
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    print(f"Данные успешно сохранены в {CSV_FILE}")


def save_csv(data):
    # Сохраняет список словарей в CSV файл.
    if not data:
        print("Нет данных для сохранения.")
        return

    headers = data[0].keys()
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def add_employee_json():
    # Добавляет нового сотрудника в JSON файл
    data = load_json()

    # Ввод данных о сотруднике
    name = input("Введите имя сотрудника: ")
    age = int(input("Введите возраст: "))
    height = float(input("Введите рост (в см): "))
    birth_year = int(input("Введите год рождения: "))

    # Ввод языков программирования (через запятую)
    languages_input = input("Введите языки программирования через запятую: ")
    languages = [lang.strip() for lang in languages_input.split(',')]

    employee = {
        "name": name,
        "age": age,
        "height": height,
        "birth_year": birth_year,
        "languages": languages
    }

    data.append(employee)
    save_json(data)
    print("Сотрудник добавлен в JSON.")


def add_employee_csv():
    # Добавляет нового сотрудника в CSV файл
    data = load_json()  # читаем текущие данные для получения заголовков
    if not data:
        # Если данных нет, запрашиваем все поля
        name = input("Введите имя сотрудника: ")
        age = int(input("Введите возраст: "))
        height = float(input("Введите рост (в см): "))
        birth_year = int(input("Введите год рождения: "))
        languages_input = input("Введите языки программирования через запятую: ")
        languages = [lang.strip() for lang in languages_input.split(',')]

        employee = {
            "name": name,
            "age": age,
            "height": height,
            "birth_year": birth_year,
            "languages": languages
        }

        save_csv([employee])

        #  добавляем в JSON для синхронизации
        save_json([employee])

        print("Данные добавлены и сохранены.")

    else:
        # Используем существующие заголовки
        headers = list(data[0].keys())

        employee = {}

        for header in headers:
            if header == 'name':
                value = input(f"Введите {header}: ")
                employee[header] = value

            elif header == 'age':
                employee[header] = int(input(f"Введите {header}: "))

            elif header == 'height':
                employee[header] = float(input(f"Введите {header}: "))

            elif header == 'birth_year':
                employee[header] = int(input(f"Введите {header}: "))

            elif header == 'languages':
                languages_input = input("Введите языки программирования через запятую: ")
                employee[header] = [lang.strip() for lang in languages_input.split(',')]

            else:
                #  добавить обработку по необходимости
                pass

        # Добавляем в JSON и сохраняем в CSV
        current_data_json = load_json()
        current_data_json.append(employee)
        save_json(current_data_json)

        # Обновляем CSV
        save_csv(current_data_json)

        print("Новый сотрудник добавлен в CSV и JSON.")


def find_employee_by_name():
    # Выводит информацию о сотруднике по имени.
    name_search = input("Введите имя для поиска: ").strip()
    data = load_json()

    found_employees = [emp for emp in data if emp.get('name') == name_search]

    if not found_employees:
        print("Сотрудник не найден.")
    else:
        for emp in found_employees:
            print(json.dumps(emp, ensure_ascii=False, indent=4))


def filter_by_language():
    # Выводит сотрудников, владеющих указанным языком программирования
    language_input = input("Введите язык программирования для фильтрации: ").strip()

    data = load_json()

    filtered_employees = []

    for emp in data:
        languages = emp.get('languages', [])

        if any(lang.lower() == language_input.lower() for lang in languages):
            filtered_employees.append(emp)

    if not filtered_employees:
        print(f"Нет сотрудников, владеющих языком {language_input}.")
    else:
        for emp in filtered_employees:
            print(json.dumps(emp, ensure_ascii=False, indent=4))


def filter_by_birth_year():
    #  средний рост сотрудников
    year_input = int(input("Введите год рождения: "))

    data = load_json()

    selected_employees = [emp for emp in data if emp.get('birth_year', 0) < year_input]

    if not selected_employees:
        print("Нет сотрудников с годом рождения меньше заданного.")
        return

    total_height = sum(emp.get('height', 0) for emp in selected_employees)

    average_height = total_height / len(selected_employees)

    print(f"Средний рост сотрудников с годом рождения меньше {year_input}: {average_height:.2f} см.")


def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить нового сотрудника (в JSON)")
        print("3. Добавить нового сотрудника (в CSV)")
        print("4. Вывести информацию о сотруднике по имени")
        print("5. Фильтр по языку программирования")
        print("6. Средний рост сотрудников с годом рождения меньше заданного")
        print("7. Выход")

        choice = input("Ваш выбор (1-7): ").strip()

        if choice == '1':
            json_to_csv()

        elif choice == '2':
            add_employee_json()

        elif choice == '3':
            add_employee_csv()

        elif choice == '4':
            find_employee_by_name()

        elif choice == '5':
            filter_by_language()

        elif choice == '6':
            filter_by_birth_year()

        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main_menu()
