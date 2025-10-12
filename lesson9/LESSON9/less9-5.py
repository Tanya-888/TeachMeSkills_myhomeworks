# урок 9

# задание 5

with open('main5', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) == 3:
            surname, name, grade_str = parts
            grade = int(grade_str)

            if grade < 3:
                print(f"{surname} {name} - {grade}")

