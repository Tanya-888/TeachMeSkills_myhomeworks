# урок 9    задание 2


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

