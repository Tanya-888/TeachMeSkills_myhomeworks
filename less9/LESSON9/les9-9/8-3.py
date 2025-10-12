# урок 9 задание 8-3

import json
import csv


def add_employee_json(json_filepath):
    name = input("Введите имя: ")
    birth_year = int(input("Введите год рождения: "))
    height = float(input("Введите рост: "))
    languages = input("Введите языки программирования (через запятую): ").split(',')

    # Убираем лишние пробелы
    languages = [lang.strip() for lang in languages]

    new_employee = {
        "name": name,
        "birth_year": birth_year,
        "height": height,
        "programming_languages": languages
    }

    # Загружаем текущие данные
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data.append(new_employee)

    # Записываем обратно
    with open(json_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Новый сотрудник добавлен в JSON.")


def add_employee_csv(csv_filepath, employee):
    # employee — это словарь с данными
    with open(csv_filepath, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "birth_year", "height", "programming_languages"])
        # Если файл пустой, напишем заголовки
        # В данном случае, лучше убедиться, что файл уже есть и содержит заголовки
        writer.writerow({
            "name": employee["name"],
            "birth_year": employee["birth_year"],
            "height": employee["height"],
            "programming_languages": ", ".join(employee["programming_languages"])
        })