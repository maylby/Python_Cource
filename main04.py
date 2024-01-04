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

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

def math(op, x, y):
    print(op(x, y))

calk1 = lambda a,b: a + b
calk2 = lambda a,b: a * b

math(calk1, 4, 6)
math(calk2, 4, 6)
math(lambda a,b: a / b, 6, 4)