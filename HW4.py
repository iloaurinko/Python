# # 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
# # (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(n):
#     return {n + n, n * n, n / 2}
#
#
# n = int(input("Введите число:"))
# print(square(n))
#
#
# # 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# #      в формате аргумент: значение. Например:
# # 	name: John
# # 	last_name: Smith
# # 	age: 35
# # 	position: web developer
# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
#
# employee(last_name='Popov', name='Max', age=40, position='web developer')
#
# # 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# #      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# my_list1 = list(filter(lambda x: x > 0, my_list))
# print(my_list1)
# # 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, my_list))
# # Чтобы получить результат перемножения только положительных значений
# print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))

# 4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
# import time
# def timer1(func):
#     def wrapper(*args, **kwargs):  # start the timer
#         start_time = time.time()  # call the decorated function
#         result = func(*args, **kwargs)  # remeasure the time
#         end_time = time.time()  # compute the elapsed time and print it
#         execution_time = end_time - start_time
#         print(f"Execution time: {execution_time} seconds")  # return the result of the decorated function execution
#         return result  # return reference to the wrapper function
#     return wrapper
# @timer1
# def summer(name):
#     return f'Hello {name}!'
# print(summer("Alex"))

# def count_execution_time(func):
#     def wrapper(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         end = time.perf_counter()
#         exec_time = end - start
#         print(f'{func.__name__} execution time is: {exec_time}')
#         return result
#     return wrapper
#
# @count_execution_time
# def greeting(name):
#     return f'Hello {name}!'

# 4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from my_calc import *
print(divide(4,0))
