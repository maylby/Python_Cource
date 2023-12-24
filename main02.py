# Знакомство с языком Python (лекции)
# Урок 2. Коллекции данных. Профилирование и отладка
# https://gb.ru/lessons/391148


# 00:04:00

""" Списки """

# list_1 = [] # пустые квадратные скобки - значит открыт "список"
# list_1 = list() # список с указанием типа данных
# list_1 = [1, 2, 3, 8] # указание данных списка
# print(*list_1) # в отсутствие "*" список выводится в квадратных скобках
# # "*" (звёздочка) удаляет квадратные скобки

# for i in list_1: # перебор списка циклом 'for'
#     print(i) # выведение 'i' при каждой итерации цикла
#     # 'i' будет принимать значения из списка
# print(len(list_1)) # функция "len" - проверка количества элементов в списке
# print(list_1[0]) # обращение к конкретному элементу списка
# # отрицательное значение в квадратных скобках [-1] - вызов элементов с конца


# 00:06:00

""" Добавление значений в список """

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # функция 'append' добавляет значение в список
# print(list_1)


# 00:07:00

''' Алгоритм заполнения списка '''

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# 00:08:00

''' Удаление последнего элемента списка '''

# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop() # возвращение последнего элемента с помощью функции 'pop'
# print(a) # вывод переменной
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]


# 00:09:00

''' Удаление конкретного элемента списка '''

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12 -> удаление нулевого элемента списка
# print(list_1) # [7, -1, 21, 0]


# 00:09:50

''' Добавление элемента на нужную позицию '''

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # первое число - позиция элемента, второе, сам элемент
# print(list_1) # [12, 7, 11, -1, 21, 0]


# 00:10:00

''' Работа со срезами в списках '''

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1 вывод первого элемента
# print(list_1[1]) # 2 вывод второго элемента списка
# print(list_1[len(list_1)-1]) # 10 -> вывод последнего элемента
# print(list_1[-1]) # 10 -> аналогично "[len(list_1)-1]"
# print(list_1[-5]) # 6 -> вывод пятого элемента с конца
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2] -> вывод от начала до 2-го элемента, исключая 2-й, т.е. 3 (тройку)
# print(list_1[len(list_1)-2:]) # [9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9] -> вывод со 2-го по 9-й элементы, исключая 9-й, т.е. 10
# print(list_1[2:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7] -> вывод от начала до конца с шагом 6 (шесть)
# print(list_1[::6]) # [1, 7] -> иной вариант записи того же самого


# 00:12:00

''' Кортежи '''

""" Кортеж - это неизменяемый список

Кортежи нужны для защиты каких-либо данных от изменений (намеренных или случайных). 
Кортеж занимает меньше места в памяти и работают быстрее, по сравнению со списками """

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,) # запятая после числа меняет тип данных с 'int' на 'tuple', теперь это кортеж
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))

# v = [1, 8, 9] # тип данных class 'list', список (?)
# print(v) # [1, 8, 9] <- вывод в квадратных скобках
# print(type(v)) # проверка типа данных

# v = tuple(v) # указываем тип данных 'tuple' (кортеж)
# print(v) # (1, 8, 9) <- вывод значений в круглых скобках - признак кортежа
# print(type(v)) # тип данных изменён на class 'tuple'

# a, b, c = v
# print(a,b,c)


""" Отличия и сходства кортежа и списка """

# t = (1, 2, 3, 5,) # признак кортежа - наличие запятой после последнего элемента
# print(t[1]) # вызов элемента по индексу
# print() # разрыв

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2 # данная команда на замену значения элемента выдаст ошибку, т.к. кортежи нельзя изменять


# 00:18:25

''' Словари '''

''' Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. 
В словаре для определения элемента используется значение ключа (строка, число).'''

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d) # выдача по запросу "(d)" -> "{'q': 'qwerty'}"

# d['w'] = 'werty'
# print(d['q']) # выдача по ключу "d['q']" -> "qwerty"
# print(d) # # выдача по запросу "(d)", с 2-мя ключами ('q', 'w') -> {'q': 'qwerty', 'w': 'werty'}

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ← типы ключей могут отличаться
# # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type' (ошибка ключа 'type' не существует)
# del dictionary['left'] # удаление элемента (функция 'del' и ключ, который хотим удалить)

# # dictionary[89] = 98998 # ключ '89' и значение "98998", соответствующее ключу 
# # print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 89: 98998} <- добавлено число

# # for item in dictionary: # перебор "словаря" циклом "for"
#     # print('{}: {}'.format(item, dictionary[item])) # вызов "ключей" и их "значений"
#     # print(item) # на экран выводятся "ключи"

# print(dictionary.items()) # вывод -> dict_items([('up', '↑'), ('down', '↓'), ('right', '→')])
# # выдача "словаря" в виде "списка" "кортежей", где указаны "ключ" и его "значение"

# for (k,v) in dictionary.items(): # вызов "ключей" и их "значений" (другая форма)
#     print(k, v) # вывод столбиком ("ключи" и их "значения")
#     # up ↑
#     # down ↓
#     # right →


# 00:24:20

""" Множества """

""" Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. 
Если есть два множества, над ними можно совершать любые стандартные операции, 
например, объединение, пересечение и разность. Давайте разберем их."""

# colors = {'red', 'green', 'blue'} # в отличие от "словарей", "множество" содержит, только перечень
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # "add" - добавление, но существующее значение добавить нельзя
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # можно добавить "add", только значение, которого нет.
# print(colors) # {'gray', 'red', 'green', 'blue'} <- добавляет в любое место перечня
# colors.remove('red') # удаление 'red'
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' <- второй запрос на удаление 'red' выдаст ошибку
# colors.discard('red') # ok <- "discard" проверяет наличие значения ('red'), 
# # если указанное значение есть, то удаляет его, если нет, пропускает строку.
# print(colors)
# colors.clear() # {} <- "clear" удаляет всё множество
# print(colors) # set() <- выдача

# q = set() # создание любого множества


# 00:27:00

""" Операции со множествами в Python: """

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} <- передача значений множества "а" множеству "с"
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} <- объедитнение уникальных значений множеств "a", "b"
# i = a.intersection(b) # i = {8, 2, 5} <- пересечение, вывод элементов, кои есть в обоих множествах
# dl = a.difference(b) # dl = {1, 3} <- разность, вычитаем из "а" значения множества "b" (2, 5, 8)
# dr = b.difference(a) # dr = {13, 21} <- разность, вычитаем из "b" совпадающие значения "a" (2, 5, 8)
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
# # сначала находим пересечение "intersection" множеств "a" и "b" (последняя функция),
# # затем, по порядку, объединяем ("union") множества "a" и "b",
# # после этого вычитаем ("difference") из объединения множеств "a" и "b" их пересечение


# 00:29:00

""" Неизменяемое или замороженное множество(frozenset) — 
множество, с которым не будут работать методы удаления и добавления."""

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# 00:30:00

""" Коллекции данных 
    
№  Тип данных         изменяемость     индексированность       уникальность      создаём
1. Список (list)           +                   +                   -             [], list()
2. Кортеж (tuple)          -                   +                   -             (), tuple()
3. Строка (string)         -                   +                   -             '', ""
4. Множество (set)         +                   -                   +             {elm1, elm2}, set()
5. Неизменное 
множество (frozenset)      -                   -                   +             frozenset()
6. Словари (dict)          + элементы          -                   + элементы    {}
                           - ключи                                 - ключи       {key: value}
                           + значения                              + значения    dict()
"""


# 00:31:50

""" List Comprehension """

""" У каждого языка программирования есть свои особенности и преимущества. 
Одна из культовых фишек Python — list comprehension (редко переводится на русский, 
но можно использовать определение «генератора списка»). 
Comprehension легко читать, и их используют как начинающие, так и опытные разработчики. 
List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, 
а также инструкции if-else для определения того, что в итоге окажется в финальном списке."""

''' 1. Простая ситуация — список:
'''
# list_1 = [exp for item in iterable] # 'exp' (некое значение) 'for item' (для) 'in range(n)' ('n' раз)
# # заменяет следующую запись: 
# for i in range(n): # где 'n' число повторов
#     list(i) = none # 'none' - добавляемое значение
    
''' 2. Выборка по заданному условию:
'''
# list_1 = [exp for item in iterable (if conditional)] # 'if conditional' - какое-то условие


# 00:33:00

''' Задача '''
""" Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
Решение:
1. Создать список чисел от 1 до 100 
"""
# list_1 = []
# for i in range(1, 101):
# list_1.append(i) 
# print(list_1) # [1, 2, 3,..., 100]
# # код не выдаёт результат (?)

""" Эту же функцию можно записать так:
"""
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# # код не выдаёт результат (?)