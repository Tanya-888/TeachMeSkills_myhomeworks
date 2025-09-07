# занятие 13     задание 1

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

num = int(input("Введите номер числа Фибоначчи, до которого нужно вывести последовательность: "))

# Вывод
for fib_num in fibonacci(num):
    print(fib_num)




# задание 2

def cyclic_sequence():
    numbers = [1, 2, 3]
    i = 0
    while True:
        yield numbers[i]
        i = (i + 1) % len(numbers)

def main():
    n = int(input("Введите количество чисел: "))
    gen = cyclic_sequence()
    for _ in range(n):
        print(next(gen), end=' ')
    print()

if __name__ == "__main__":
    main()




# задание 3

# Класс Pizza с атрибутами
class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        if self.onions:
            toppings.append("onions")
        if self.bacon:
            toppings.append("bacon")
        toppings_str = ", ".join(toppings) if toppings else "no toppings"
        return f"Pizza(size={self.size}, toppings={toppings_str})"


# Класс PizzaBuilder для создания пиццы
class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(
            size=self.size,
            cheese=self.cheese,
            pepperoni=self.pepperoni,
            mushrooms=self.mushrooms,
            onions=self.onions,
            bacon=self.bacon
        )


# Класс PizzaDirector управляет процессом создания пиццы
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        #  создаём пиццу с сыром, пепперони и беконом
        return self.builder.add_cheese().add_pepperoni().add_bacon().build()


# Пример
if __name__ == "__main__":
    builder = PizzaBuilder(size="Large")
    director = PizzaDirector(builder)
    pizza = director.make_pizza()
    print(pizza)

# задание 4

from abc import ABC, abstractmethod

# Абстрактный класс Animal с абстрактным методом speak
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Класс Dog, наследник Animal
class Dog(Animal):
    def speak(self):
        return "Aff"

# Класс Cat, наследник Animal
class Cat(Animal):
    def speak(self):
        return "Meow"

# Фабрика для создания объектов Animal
class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Пример
factory = AnimalFactory()

dog = factory.create_animal("dog")
print(dog.speak())

cat = factory.create_animal("cat")
print(cat.speak())



# задание 5

# Интерфейс стратегии (необязательно, просто для понимания)
class Operation:
    def execute(self, a, b):
        pass

# Конкретные стратегии
class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль запрещено"
        return a / b

# Класс Calculator
class Calculator:
    def __init__(self, strategy: Operation):
        self.strategy = strategy

    def set_strategy(self, strategy: Operation):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)

# Пример
if __name__ == "__main__":
    calc = Calculator(Addition())
    print(calc.calculate(10, 5))  # 15

    calc.set_strategy(Subtraction())
    print(calc.calculate(10, 5))  # 5

    calc.set_strategy(Multiplication())
    print(calc.calculate(10, 5))  # 50

    calc.set_strategy(Division())
    print(calc.calculate(10, 5))  # 2.0
    print(calc.calculate(10, 0))  #  деление на ноль