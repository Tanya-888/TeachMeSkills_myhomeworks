# урок 9 задание 8-5

import json

def filter_by_language(json_filepath):
    language = input("Введите язык программирования: ").strip()
    with open(json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    filtered = [emp for emp in data if language in emp["programming_languages"]]
    if filtered:
        for emp in filtered:
            print(emp)
    else:
        print("Нет сотрудников, владеющих этим языком.")