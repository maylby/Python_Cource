# Знакомство с языком Python (лекции)
# Урок 4. Функции высшего порядка, работа с файлами
# https://gb.ru/lessons/391150

""" Содержание лекции """

"""
    ● Анонимные, lambda-функции
    ● Функция map
    ● Функция filter
    ● Функция zip
    ● Функция enumerate
    ● Файлы
    ● Модуль os
    ● Модуль shutil
"""

# 00:02:00

# x = int(input('Input variable X: ', ))
# def f(x):
#     return x*x
# a = f # замена 'f' на 'a'
# print(type(a))  # проверка типа данных
#                 # выдаёт запись - class 'function', т.е.
#                 # обе переменные 'f' и 'a' после передачи значения 'f' 
#                 # ссылаются на какую-то оперативную память ПК,
#                 # где записана данная функция
# print(a(x))
# print(f(x))



# 00:04:00

""" Калькулятор """

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 6)
# math(calk2, 5, 6)


# 00:06:20

""" Анонимные, lambda-функции """

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b: a + b
# calk2 = lambda a,b: a * b

# math(calk1, 4, 6)
# math(calk2, 4, 6)
# math(lambda a,b: a / b, 6, 4)



# 00:08:30

""" Задача для самостоятельного решения """
"""
1. В списке хранятся числа. 
Нужно выбрать только чётные числа 
и составить список пар (число; квадрат числа). 
"""
# # Пример: 1 2 3 5 8 15 23 38
# # Получить: [(2, 4), (8, 64), (38, 1444)]
# # Решение:

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# # out = [] # вариант 1 записи передачи списка (data) переменной 'out'
# out = list() # вариант 2 передачи переменной 'out' списка (data),
#              # которым будем оперировать 
# for i in data : # пербор элементов списка (data)
#     if i % 2 == 0: # если число чётное, то заносим его в 'out'
#         out.append((i, i ** 2)) # запись в виде кортежа (число, его квадрат)
# print(data) # начальный список -> [1, 2, 3, 5, 8, 15, 23, 38]
# print(out) # итоговый список -> [(2, 4), (8, 64), (38, 1444)]



# 00:15:00

""" Решение задачи с помощью lambda-функции """

# def select(f, col):
#     return [f(x) for x in col]  # возврат списка, к каждому элементу которого
#                                 # применена функция f(x)
# def where(f, col):
#     return [x for x in col if f(x)] # возврат значений, 
#                                     # прошедших проверку условия f(x)
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data) # переменной 'res' передаём начальный список (data)
# print(res)
# res = where(lambda x: x % 2 == 0, res) # поиск только чётных значений
# print(res)
# res = list(select(lambda x: (x, x**2), res)) # формирование кортежа 
#                                              # из значений и их квадратов
# print(res)



# 00:19:00

""" Функция map """
"""
Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.
Есть набор данных. Функция map позволяет увеличить каждый объект на 10.
"""

# list_1 = [x for x in range(1, 10)]  # создание с помощью функции 'range' списка элементов,
#                                     # состоящего из чисел от 1 до 10 
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1)) # функции 'map' передаём, функцию 'lambda',
#                                              # преобразующую элементы исходного списка,
#                                              # которые передаём функции 'list'
#                                              # для создания нового списка 'list_1'
# print(list_1)



# 00:20:35

""" 
Задача: 
C клавиатуры вводится некий набор чисел, 
в качестве разделителя используется пробел. 
Этот набор чисел будет считан в качестве строки. 
Как превратить list строк в list чисел?
"""

""" 1. Функция строка.split() - убирает все пробелы 
и создает список из значений строки, например:
"""

# data = '1 2 3 5 8 15 23 38'
# print(data)

# data = data.split()
# print(data)


# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']


""" 2. Теперь вернемся к задаче. С помощью функции map(): 
"""

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int, data.split()))
# print(data)

# data = list(map(int,input().split()))
# print(data)


""" Задача из раздела lambda-функции (00:15:00)"""

# def select(f, col): return [f(x) for x in col] # замена записи функцией 'map'
def where(f, col): return [x for x in col if f(x)] 

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data) # замена функции 'select', прописаной явно,
                     # функцией 'map', прописанной где-то в модуле Pyhton, т.е.
                     # 'map' и 'select' - это одна и та же функция возврата списка,
                     # к каждому элементу которого применена функция f(x)
print(data)
res = where(lambda x: x % 2 == 0, res) 
print(res)
res = list(map(lambda x: (x, x**2), res)) # 'map' стоит вместо 'select'

print(res)