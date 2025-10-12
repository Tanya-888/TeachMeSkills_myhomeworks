# урок 9 задание 8-1

import json
import csv


def json_to_csv(json_filepath, csv_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Определение заголовков
    headers = ["name", "birth_year", "height", "programming_languages"]

    with open(csv_filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for employee in data:
            # Преобразуем список языков в строку
            employee_copy = employee.copy()
            employee_copy["programming_languages"] = ", ".join(employee["programming_languages"])
            writer.writerow(employee_copy)

# Пример вызова:
# json_to_csv('employees.json', 'employees.csv')