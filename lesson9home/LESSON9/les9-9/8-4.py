# урок 9 задание 8-4

import json

def find_employee_by_name(json_filepath):
    name_to_find = input("Введите имя сотрудника для поиска: ")
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for employee in data:
        if employee["name"].lower() == name_to_find.lower():
            print(employee)
            return
    print("Сотрудник не найден.")