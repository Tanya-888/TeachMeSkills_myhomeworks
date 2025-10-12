# урок 9 задание 8-6

import json

def filter_by_birth_year(json_filepath):
    year = int(input("Введите год рождения: "))
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    filtered = [emp for emp in data if emp["birth_year"] < year]
    if filtered:
        total_height = sum(emp["height"] for emp in filtered)
        average_height = total_height / len(filtered)
        print(f"Средний рост сотрудников, родившихся раньше {year}: {average_height:.2f}")
    else:
        print("Нет сотрудников по условию.")