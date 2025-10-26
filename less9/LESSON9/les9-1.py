# урок 9    задание 1



import os
import platform
import shutil

def main():
                               # 1. Вывести имя  ОС
    os_name = platform.system()
    print(f"Имя вашей ОС: {os_name}")

                            # 2. Вывести путь до текущей папки
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")

                         # 3. Рассортировать файлы по расширениям

    files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

                           # Создать словарь расширений и соответствующих папок
    ext_dirs = {}
    for filename in files:
        ext = os.path.splitext(filename)[1].lower()
        if ext:
            dir_name = ext[1:]  # убрать точку
        else:
            dir_name = 'без_расширения'
        ext_dirs.setdefault(dir_name, []).append(filename)

    # Для каждого расширения создать папку и переместить файлы
    for ext, filenames in ext_dirs.items():
        target_dir = os.path.join(current_dir, ext)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for filename in filenames:
            src_path = os.path.join(current_dir, filename)
            dst_path = os.path.join(target_dir, filename)
            shutil.move(src_path, dst_path)

                          # 4.  Выводим сообщение о количестве и размере файлов
        total_size_bytes = sum(os.path.getsize(os.path.join(target_dir, f)) for f in filenames)
        total_size_gb = total_size_bytes / (1024 ** 3)  # перевод в гигабайты

        print(f"В папке с {ext} файлами перемещено {len(filenames)} файлов, их размер – {total_size_gb:.2f} ГБ.")

                           # 5. Переименовать один файл в каждой поддиректории (если они есть)
        if filenames:
            old_name = filenames[0]
            old_path = os.path.join(target_dir, old_name)
            new_name = 'some_' + old_name
            new_path = os.path.join(target_dir, new_name)
            os.rename(old_path, new_path)
            print(f"Файл {old_name} был переименован в {new_name}")

if __name__ == "__main__":
    main()
