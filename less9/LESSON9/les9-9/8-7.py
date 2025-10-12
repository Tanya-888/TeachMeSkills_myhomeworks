# урок 9 задание 8-7

import json
import os
from json_to_csv import json_to_csv
from save_to_csv import save_employees_to_csv
from add_employee import add_employee_json, add_employee_csv
from find_employee import find_employee_by_name
from filter_by_language import filter_by_language
from filter_by_birth_year import filter_by_birth_year

JSON_FILE = 'employees.json'
CSV_FILE = 'employees.csv'

def load_json():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    while True:
        print("\nМеню:")
        print("1. Преобразовать JSON в CSV")
        print("2. Сохранить текущих данных в CSV")
        print("3. Добавить нового сотрудника")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Средний рост по году рождения")
        print("7. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            json_to_csv(JSON_FILE, CSV_FILE)
            print("Преобразование завершено.")
        elif choice == '2':
            data = None
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            save_employees_to_csv(CSV_FILE, data)
            print("Данные сохранены в CSV.")
        elif choice == '3':
            add_employee_json(JSON_FILE)
            # Обновление CSV
            data = load_json()
            save_employees_to_csv(CSV_FILE, data)
        elif choice == '4':
            find_employee_by_name(JSON_FILE)
        elif choice == '5':
            filter_by_language(JSON_FILE)
        elif choice == '6':
            filter_by_birth_year(JSON_FILE)
        elif choice == '7':
            print("Выход.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == '__main__':
    # Проверка наличия файлов
    if not os.path.exists(JSON_FILE):
        print(f"Файл {JSON_FILE} не найден.")
    elif not os.path.exists(CSV_FILE):
        # Можно автоматически создать пустой CSV с заголовками
        with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "birth_year", "height", "programming_languages"])
            writer.writeheader()
    main()