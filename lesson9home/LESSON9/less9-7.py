# урок 9

# задание 7

                  # Открываем файл .txt
with open('some.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

                  # Обрабатываем  строки
encrypted_lines = []
for i, line in enumerate(lines, start=1):
    line = line.rstrip('\n')  # Удаляем символ переноса строки
    encrypted_line = ''
    for char in line:
        if char.isalpha():
                                # Определяем заглавные и строчные буквы
            base = ord('A') if char.isupper() else ord('a')
                                   # Символ с учетом шага
            shifted_char = chr((ord(char) - base + i) % 26 + base)
            encrypted_line += shifted_char
        else:
                                 # Если символ не буква, оставляем без изменений
            encrypted_line += char
    encrypted_lines.append(encrypted_line)

                             # Вывод
for line in encrypted_lines:
    print(line)
