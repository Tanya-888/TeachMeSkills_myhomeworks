import time
import threading
import multiprocessing
import requests
import math
import os


                     # Задача 1

# последовательная версия
def math_task(x):
    result = 0
    for i in range(10 ** 6):
        result += math.sin(x) * math.cos(x) + math.log(i + 1)
    return result


def run_sequential_math(N):
    print("Запуск последовательной математики")
    start_time = time.time()
    for i in range(N):
        math_task(i + 1)
    end_time = time.time()
    print(f"sequential: {end_time - start_time:.2f} сек")

# поточная версия
def thread_math_task(x):
    return math_task(x)

def run_thread_math(N):
    print("Запуск потоковой математики")
    threads = []
    start_time = time.time()
    for i in range(N):
        t = threading.Thread(target=thread_math_task, args=(i + 1,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"streaming: {end_time - start_time:.2f} сек")

# процессная версия
def process_math_task(x):
    return math_task(x)

def run_process_math(N):
    print("Запуск процессорной математики")
    processes = []
    start_time = time.time()
    for i in range(N):
        p = multiprocessing.Process(target=process_math_task, args=(i + 1,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    print(f"process: {end_time - start_time:.2f} сек")


            # Задача 2

# сайты для запросов
URLS = [
    'https://www.google.com',
    'https://www.wikipedia.org',
    'https://www.python.org',
]

# последовательная
def get_request(url):
    try:
        requests.get(url)
    except:
        pass

def run_sequential_get(N):
    print("Запуск последовательных GET-запросов")
    start_time = time.time()
    for _ in range(N):
        for url in URLS:
            get_request(url)
    end_time = time.time()
    print(f"sequential GET: {end_time - start_time:.2f} сек")

# поточная
def thread_get_request(url):
    get_request(url)

def run_thread_get(N):
    print("Запуск потоковых GET-запросов")
    threads = []
    start_time = time.time()
    for _ in range(N):
        for url in URLS:
            t = threading.Thread(target=thread_get_request, args=(url,))
            threads.append(t)
            t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f"streaming GET: {end_time - start_time:.2f} сек")

# процессная
def process_get_request(url):
    get_request(url)

def run_process_get(N):
    print("Запуск процессных GET-запросов")
    processes = []
    start_time = time.time()
    for _ in range(N):
        for url in URLS:
            p = multiprocessing.Process(target=process_get_request, args=(url,))
            processes.append(p)
            p.start()
    for p in processes:
        p.join()
    end_time = time.time()
    print(f"process GET: {end_time - start_time:.2f} сек")

# запуск и сравнение
if __name__ == "__main__":
    N = 7

# Задача 1
    run_sequential_math(N)
    run_thread_math(N)
    run_process_math(N)

# Задача 2
    run_sequential_get(N)
    run_thread_get(N)
    run_process_get(N)