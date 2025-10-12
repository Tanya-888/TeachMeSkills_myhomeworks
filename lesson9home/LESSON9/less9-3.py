# урок 9    задание 3


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

