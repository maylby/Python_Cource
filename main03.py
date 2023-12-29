# Знакомство с языком Python (лекции)
# Урок 3. Функции, рекурсия, алгоритмы
# https://gb.ru/lessons/391149


""" Функции """
"""
Функция — это фрагмент программы, используемый многократно.
Мы знакомы уже с функциями в C#, давайте теперь посмотрим, как
создаются и используются функции внутри Python 
P.S. 
В Python не выделяются функции и процедуры, как 
самостоятельные единицы, они объединены в одно понятие "функция".
"""
# def function_name(x):
#     body line 1
#     ...
#     body line n
#     optional return


""" Задача """
"""
Необходимо создать функцию sumNumbers(n), которая будет
считать сумму всех элементов от 1 до n.

Очень важно понимать одну вещь, 
сколько аргументов мы передаем, столько и принимаем. 
Или наоборот сколько аргументов мы принимаем, столько и передаем.
В нашем случае функция sumNumbers принимает 1 аргумент(n).

Решение:
"""
# n = 5   # передача значения переменной 'n'
#         # передать значение переменной можно при вызове функции (см. ниже)
# def sum_numbers(n, y = 'Hello'): # параметр 'def' сообщает Python, что задана функция
#     print(y)
#                     # с именем 'sum_numbers'
#                     # в Python определение типа переменных динамичное,
#                     # указывать тип переменной не нужно                  
#     summa = 0 # создание переменной 'summa',
#               # с указанием текущего значения равного нулю
#     for i in range(1, n+1): # цикл перебора чисел в промежутке от 1 до n+1
#         summa += i # увеличение значения переменной (summa) на значение индекса (i)
#     # print(summa) # вывод результата суммирования
#     return summa # возврат (return) суммы, вместо её вывода (print)
#                  # при появлении оператора 'return', программа завершает работу
# a = sum_numbers(n, 'qwert')  # создание переменной 'a' 
#                     # и передача ей значения функции 'sum_numbers(n)'
# print(a) # вывод значения переменной 'a'
# print(sum_numbers(n))   # вывывод (print) функции одновременно с её вызовом (sum_numbers)
#                         # и указанием либо конкретного значения переменной 'n', например, (5)
#                         # либо символа переменной (n) в скобках,
#                         # если её значение было задано вначале (n = 5)


# 00:07:30

""" Функция принимающая любое кодичество аргументов """

# def sum_str(*a): # Что делает эта функция?
#                  # Какой в ней практический смысл?
#                  # Где и для чего её можно применить?
#     res = ''
#     for i in a:
#         res += i
#     return res
# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','r','f'))
# # print(sum_str(a, s, d, f)) # передача открытых, не заковыченных знаков, выдаст ошибку
# # print(sum_str(1, 3, 4)) # аналогично, передача открытых числовых значений, тоже выдаст ошибку
# print(sum_str('1', '3', '4'))   # передача чисел в кавычках допустима,
#                                 # ошибки не возникает


# 00:09:20

""" Модульность """
"""
Как работает, например, функция .append?
Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем.
Все дело в том что, это функция автоматически срабатывает, 
и чтобы ей пользоваться ничего дополнительно писать не надо.
Представьте себе такую ситуацию, что Вы создаете огромный проект и у Вас
имеется большое количество функций, к примеру 5 функций работают со
словарями, 18 со списками и тд. и у каждой функции свой алгоритм, но их
объединяет работа с одной коллекцией данных. Согласитесь неудобно работать в
таком большом файле, где около 80 функций, очень легко потеряться и на
перемотку кода Вы будете терять драгоценное время. Решение данной проблемы
есть. Давайте будем создавать отдельные файлы, где будут находиться только
функции, и эти функции при необходимости вызывать из главного файла.
"""

''' 
Код скопирован в файл "modul1.py" 
'''
# a = input('input A: ', )
# b = input('input B: ', )
# def max1(a, b):
#     if a > b: return a
#     return b
#     # else: return b  # т.к. функция return прерывает работу программы,
#                     # функция else становится лишней, поскольку,
#                     # в случае, если a > b, то код возвратит 'a',
#                     # после чего программа прервётся,
#                     # но если a < b, то код продолжит работу и возвратит 'b',
#                     # т.е. else, можно пропустить, оптимизировав код.
# print(max1(a, b))

''' 
Импорт функции 

Способ 1
'''
a = input('input A: ', ) # ввод данных (a) пользователем
b = input('input B: ', ) # ввод данных (b) пользователем

import modul1 # вызов кода из файла зранения модулей
print(modul1.max1(a, b)) # вывод результата работы кода

'''
Способ 2
'''
from modul1 import max1 # обращение к файлу (modul1)
                        # указание импорта конкретной функции (max1) 
print(max1(a, b)) # в этом случае, указывать файл хранения (modul1) не нужно
                 # вверху ввод (input) данных (a, b)