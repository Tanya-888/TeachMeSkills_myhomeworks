class Date:
    def __init__(self, day, month, year, hour=0, minute=0):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year} {self.hour:02d}:{self.minute:02d}"

class Task:
    def __init__(self, title, description, due_date: Date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "В процессе"
        return f"Задача: {self.title}\nОписание: {self.description}\nСрок: {self.due_date}\nСтатус: {status}"

class Meeting:
    def __init__(self, subject, date: Date, location):
        self.subject = subject
        self.date = date
        self.location = location

    def __str__(self):
        return f"Встреча: {self.subject}\nДата и время: {self.date}\nМесто: {self.location}"

class Planner:
    def __init__(self):
        self.tasks = []
        self.meetings = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_meeting(self, meeting: Meeting):
        self.meetings.append(meeting)

    def list_tasks(self):
        if not self.tasks:
            print("Задачи отсутствуют.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}\n")

    def list_meetings(self):
        if not self.meetings:
            print("Встречи отсутствуют.")
        for i, meeting in enumerate(self.meetings, 1):
            print(f"{i}. {meeting}\n")

class User:
    def __init__(self, name):
        self.name = name
        self.planner = Planner()

    def __str__(self):
        return f"Пользователь: {self.name}"

class App:
    def __init__(self):
        self.user = None

    def run(self):
        print("Добро пожаловать в планер для юриста!")
        name = input("Введите ваше имя: ")
        self.user = User(name)
        while True:
            print("\nВыберите действие:")
            print("1. Добавить задачу")
            print("2. Добавить встречу")
            print("3. Показать задачи")
            print("4. Показать встречи")
            print("5. Выход")
            choice = input("Введите номер действия: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.add_meeting()
            elif choice == "3":
                self.user.planner.list_tasks()
            elif choice == "4":
                self.user.planner.list_meetings()
            elif choice == "5":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    def add_task(self):
        title = input("Название задачи: ")
        description = input("Описание задачи: ")
        due_date = self.input_date("Введите срок задачи")
        task = Task(title, description, due_date)
        self.user.planner.add_task(task)
        print("Задача добавлена.")

    def add_meeting(self):
        subject = input("Тема встречи: ")
        date = self.input_date("Введите дату и время встречи")
        location = input("Место встречи: ")
        meeting = Meeting(subject, date, location)
        self.user.planner.add_meeting(meeting)
        print("Встреча добавлена.")

    def input_date(self, prompt):
        print(prompt)
        day = int(input("День (1-31): "))
        month = int(input("Месяц (1-12): "))
        year = int(input("Год (например, 2025): "))
        hour = int(input("Час (0-23): "))
        minute = int(input("Минута (0-59): "))
        return Date(day, month, year, hour, minute)

if __name__ == "__main__":
    app = App()
    app.run()