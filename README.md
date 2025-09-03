# мои домашние задания в TMS

# задание 1 урок 11

class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"

# Пример
soda1 = Soda("клубничным")
print(soda1)  # У вас газировка с клубничным вкусом

soda2 = Soda()
print(soda2)  # У вас обычная газировка



# задание 2

class Math:
    def addition(self, a, b):
        result = a + b
        print(f"{a} + {b} = {result}")

    def subtraction(self, a, b):
        result = a - b
        print(f"{a} - {b} = {result}")

    def multiplication(self, a, b):
        result = a * b
        print(f"{a} * {b} = {result}")

    def division(self, a, b):
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Деление на ноль невозможно")



# задание 3

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведён")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color


car = Car("Красный", "универсал", 2024)
car.start()  # Вывод: Автомобиль заведён
car.set_color("Черный")
car.set_type("седан")
car.set_year(2021)
print(f"Цвет: {car.color}, Тип: {car.type}, Год: {car.year}")
car.stop()   # Вывод: Автомобиль заглушен



# задание 4

import math

class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):    # возвращает объем сферы V = 4/3 * π * r^3

        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):        # возвращает площадь внешней поверхности сферы  S = 4 * π * r^2

        return 4 * math.pi * self.radius ** 2

    def get_radius(self):    # возвращает текущий радиус сферы

        return self.radius

    def get_center(self):     # возвращает кортеж с координатами центра сферы

        return self.center

    def set_radius(self, radius):           # новый радиус сферы

        self.radius = radius

    def set_center(self, x, y, z):              #  новые координаты центра сферы

        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):

        # Проверяет, находится ли точка внутри сферы
        # точка внутри или на границе: расстояние до центра <= радиуса

        dx = x - self.center[0]
        dy = y - self.center[1]
        dz = z - self.center[2]

        distance_squared = dx ** 2 + dy ** 2 + dz ** 2
        return distance_squared <= self.radius ** 2



# задание 5

class SuperStr(str):
    def is_repeatance(self, s):
        # Если строка s пустая, возвращаем False
        if not s:
            return False
        # Проверяем, что текущая строка может быть получена повторением s
        # проверяем, что длина текущей строки делится на длину s
        if len(self) % len(s) != 0:
            return False
        # Строим строку из повторений s и сравниваем с текущей
        if self == s * (len(self) // len(s)):
            return True
        return False

    def is_palindrom(self):
        # Палиндром вне зависимости от регистра
        lower_str = self.lower()
        return lower_str == lower_str[::-1]