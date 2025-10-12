# урок 9

# задание 6

import re

total_sum = 0
              #открываем файл .txt
with open('hello_some.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = re.findall(r'\d+', line)
        total_sum += sum(int(num) for num in numbers)

print(total_sum)