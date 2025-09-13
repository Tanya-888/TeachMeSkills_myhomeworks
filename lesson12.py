# задание 1 урок 12


class Tovar:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    # доступ к закрытым полям
    @property
    def name(self):
        return self.__name

    @property
    def shop(self):
        return self.__shop

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price} руб."

    # Перегрузка сложения по цене
    def __add__(self, other):
        if isinstance(other, Tovar):
            return self.__price + other.__price
        return NotImplemented


class Sklad:
    def __init__(self):
        self.__tovary = []

    def add_tovar(self, tovar):
        self.__tovary.append(tovar)

    def get_tovar_by_index(self, index):
        if 0 <= index < len(self.__tovary):
            return str(self.__tovary[index])
        else:
            return "Индекс вне диапазона"

    def get_tovar_by_name(self, name):
        for tovar in self.__tovary:
            if tovar.name == name:
                return str(tovar)
        return "Товар не найден"

    def sort_by_name(self):
        self.__tovary.sort(key=lambda t: t.name)

    def sort_by_shop(self):
        self.__tovary.sort(key=lambda t: t.shop)

    def sort_by_price(self):
        self.__tovary.sort(key=lambda t: t.price)

# Пример

# Создаем склад и добавляем товары
sklad = Sklad()
sklad.add_tovar(Tovar("Хлеб", "Магазин1", 10))
sklad.add_tovar(Tovar("Молоко", "Магазин2", 60))
sklad.add_tovar(Tovar("Творог", "Магазин1", 200))

# Вывод по индексу
print(sklad.get_tovar_by_index(1))  # Молоко

# Вывод по имени товара
print(sklad.get_tovar_by_name("Творог"))  # Творог

# Сортировка по названию и вывод
sklad.sort_by_name()
for i in range(3):
    print(sklad.get_tovar_by_index(i))

# Сортировка по магазину и вывод
sklad.sort_by_shop()
for i in range(3):
    print(sklad.get_tovar_by_index(i))

# Сортировка по цене и вывод
sklad.sort_by_price()
for i in range(3):
    print(sklad.get_tovar_by_index(i))

# Перегрузка сложения товаров по цене
print("Общая цена двух товаров:", sklad._Sklad__tovary[0] + sklad._Sklad__tovary[1])  # сумма цен первых двух товаров




# задание 2

class ПчёлоСлон:
    def __init__(self, пчела, слон):
        self.пчела = пчела
        self.слон = слон

    def Fly(self):
        return self.пчела >= self.слон

    def Trumpet(self):
        if self.слон >= self.пчела:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def Eat(self, meal, value):
        if meal not in ["nectar", "grass"]:
            return  # Неверный тип еды, ничего не делаем

        if meal == "nectar":
            # Уменьшаем часть слона, увеличиваем пчелу
            new_слон = max(self.слон - value, 0)
            delta = self.слон - new_слон
            self.слон = new_слон
            self.пчела = min(self.пчела + delta, 100)
        else:  # grass
            # Увеличиваем часть слона, уменьшаем пчелу
            new_пчела = max(self.пчела - value, 0)
            delta = new_пчела - self.пчела
            self.пчела = new_пчела
            self.слон = min(self.слон + delta, 100)


# задание 3

class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []  # список фамилий пассажиров
        self.has_free_seats = True
        # словарь мест: ключ - место (номер), значение - фамилия или None
        self.seats = {i: None for i in range(1, max_seats + 1)}

    def update_free_seats(self):
        # Обновляем флаг наличия свободных мест
        self.has_free_seats = any(v is None for v in self.seats.values())

    def board_passenger(self, surname):
        # Посадка пассажира по фамилии
        for seat_number, occupant in self.seats.items():
            if occupant is None:
                self.seats[seat_number] = surname
                self.passengers.append(surname)
                self.update_free_seats()
                print(f"{surname} посажен на место {seat_number}")
                return
        print("Нет свободных мест!")

    def disembark_passenger(self, surname):
        # Высадка пассажира по фамилии
        for seat_number, occupant in self.seats.items():
            if occupant == surname:
                self.seats[seat_number] = None
                if surname in self.passengers:
                    self.passengers.remove(surname)
                self.update_free_seats()
                print(f"{surname} высажен с места {seat_number}")
                return
        print(f"Пассажир {surname} не найден в автобусе.")

    def increase_speed(self, delta):
        new_speed = min(self.speed + delta, self.max_speed)
        print(f"Увеличение скорости с {self.speed} до {new_speed}")
        self.speed = new_speed

    def decrease_speed(self, delta):
        new_speed = max(self.speed - delta, 0)
        print(f"Уменьшение скорости с {self.speed} до {new_speed}")
        self.speed = new_speed

    def __contains__(self, item):
        # Проверка наличия пассажира по фамилии
        return item in self.passengers

    def __iadd__(self, other):
        # Посадка пассажира (добавление через +=)
        if isinstance(other, str):
            self.board_passenger(other)
            return self
        else:
            raise ValueError("Можно посадить только по фамилии")

    def __isub__(self, other):
        # Высадка пассажира (удаление через -=)
        if isinstance(other, str):
            self.disembark_passenger(other)
            return self
        else:
            raise ValueError("Можно высадить только по фамилии")

# Пример использования:
bus = Bus(max_seats=15, max_speed=100)

# Посадка пассажиров
bus += "Иванов"
bus += "Сидоров"

# Проверка наличия пассажира
print("Иванов" in bus)  # True

# Увеличение скорости
bus.increase_speed(50)

# Уменьшение скорости
bus.decrease_speed(20)

# Высадка пассажира
bus -= "Иванов"

# Проверка наличия после высадки
print("Иванов" in bus)  # False



