# урок 9 задание 8-2

import csv

def save_employees_to_csv(csv_filepath, data):
    headers = ["name", "birth_year", "height", "programming_languages"]
    with open(csv_filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for employee in data:
            employee_copy = employee.copy()
            employee_copy["programming_languages"] = ", ".join(employee["programming_languages"])
            writer.writerow(employee_copy)

