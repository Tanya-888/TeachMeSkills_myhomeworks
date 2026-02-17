import threading
import time
import random

# Задача 1

class Order:
    def __init__(self, order_id, required_resources, processing_time):
        self.order_id = order_id
        self.required_resources = required_resources
        self.processing_time = processing_time
        self.status = 'Pending'

class Worker:
    def __init__(self, worker_id, resource_semaphore, lock):
        self.worker_id = worker_id
        self.resource_semaphore = resource_semaphore
        self.lock = lock

    def process_order(self, order):
        # обработка заказа
        print(f"Работник {self.worker_id} начал обработку заказа {order.order_id}")
        time.sleep(order.processing_time)
        with self.lock:
            order.status = 'Completed'
            print(f"Работник {self.worker_id} завершил заказ {order.order_id}")

def handle_orders(orders, worker, order_queue, queue_lock):
    while True:
        with queue_lock:
            if not orders:
                break
            order = orders.pop(0)
        #  захват ресурса
        with worker.resource_semaphore:
            with worker.lock:
                # симуляция проверки ресурсов
                print(f"Работник {worker.worker_id} обрабатывает заказ {order.order_id}")
                worker.process_order(order)

def task_orders():
    # Создаем список заказов
    orders = [Order(i, required_resources=1, processing_time=random.uniform(0.5, 1.5)) for i in range(10)]
    order_queue = orders.copy()
    queue_lock = threading.Lock()

    # Создаем семафор
    max_workers = 3
    resource_semaphore = threading.Semaphore(max_workers)

    # Создаем мьютекс
    lock = threading.Lock()

    # Создаем работников
    workers = [Worker(i, resource_semaphore, lock) for i in range(5)]

    threads = []
    for worker in workers:
        t = threading.Thread(target=handle_orders, args=(orders, worker, order_queue, queue_lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Заказы обработаны.\n")




# Задача 2

class Seance:
    def __init__(self, film_name, timeslot, total_seats):
        self.film_name = film_name
        self.timeslot = timeslot
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.lock = threading.Lock()

class Cinema:
    def __init__(self):
        self.films = {
            'Film A': [Seance('Film A', '12:00', 10), Seance('Film A', '15:00', 8)],
            'Film B': [Seance('Film B', '13:00', 12), Seance('Film B', '16:00', 10)],
        }
        self.condition = threading.Condition()

    def list_films(self):
        return list(self.films.keys())

    def list_seances(self, film_name):
        return self.films.get(film_name, [])

    def reserve_seat(self, film_name, timeslot):
        seances = self.films.get(film_name)
        if not seances:
            print("Фильм не найден")
            return False

        for seance in seances:
            if seance.timeslot == timeslot:
                with seance.lock:
                    if seance.available_seats > 0:
                        seance.available_seats -= 1
                        print(f"Забронировано место на '{film_name}' в {timeslot}. Осталось {seance.available_seats}")
                        return True
                    else:
                        print(f"Места на '{film_name}' в {timeslot} закончились.")
                        return False
        print("Такой сеанс не найден.")
        return False

def booking_process(cinema, user_id):
    # выбор фильма и сеанса
    films = cinema.list_films()
    film_choice = random.choice(films)
    seances = cinema.list_seances(film_choice)
    seance_choice = random.choice(seances).timeslot
    print(f"Пользователь {user_id} пытается забронировать место на '{film_choice}' в {seance_choice}")
    success = cinema.reserve_seat(film_choice, seance_choice)
    if success:
        print(f"Пользователь {user_id} успешно забронировал место.")
    else:
        print(f"Пользователь {user_id} не смог забронировать место.")

def task_booking():
    cinema = Cinema()
    max_concurrent_requests = 5
    semaphore = threading.Semaphore(max_concurrent_requests)

    threads = []

    for user_id in range(10):  # пользователи
        t = threading.Thread(target=lambda uid=user_id: (semaphore.acquire(),
                                                          booking_process(cinema, uid),
                                                          semaphore.release()))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Бронирование завершено.\n")


#  запуск обеих задач

if __name__ == "__main__":
    print("Задача 1: Обработка заказов с ограниченными ресурсами")
    task_orders()

    print("Задача 2: Система бронирования билетов")
    task_booking()