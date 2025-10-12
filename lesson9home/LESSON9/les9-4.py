# урок 9

# задание 4


import os
import re

def load_stop_words(filename):
                                      # Загружает список запрещённых слов из файла
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

        stop_words = content.strip().split()

        stop_words = [word.lower() for word in stop_words]
    return stop_words

def censor_text(input_filename, stop_words):
                                          
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





