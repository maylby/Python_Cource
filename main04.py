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

# # 00:02:00

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



# # 00:04:00

""" Калькулятор """

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk1, 5, 6)
# math(calk2, 5, 6)


# # 00:06:20

""" Анонимные, lambda-функции """

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b: a + b
# calk2 = lambda a,b: a * b

# math(calk1, 4, 6)
# math(calk2, 4, 6)
# math(lambda a,b: a / b, 6, 4)



# # 00:08:30

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



# # 00:15:00

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



# # 00:19:00

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



# # 00:20:35

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

# # def select(f, col): return [f(x) for x in col] # замена записи функцией 'map'
# def where(f, col): 
#     return [x for x in col if f(x)] 

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) # замена функции 'select', прописаной явно,
#                      # функцией 'map', прописанной где-то в модуле Pyhton, т.е.
#                      # 'map' и 'select' - это одна и та же функция возврата списка,
#                      # к каждому элементу которого применена функция f(x)
# print(data)
# res = where(lambda x: x % 2 == 0, res) 
# print(res)
# res = list(map(lambda x: (x, x**2), res)) # 'map' стоит вместо 'select'
# print(res)


# # 00:24:00

""" Функция filter """

"""
Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для которых функция вернула 'True'.
"""
# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]

"""
Все данные, находящиеся внутри внутри 'filter()', 
проходят через функцию (lambda):
"""
# lambda x: x % 2 == 0

"""
Т.е., проводится проверка чётности числа (получение остатка 0 при делении на 2), 
а итоговые данные преобразуются в список, с помощью функции list().
"""


# # 00:25:00

data = [15, 65, 9, 36, 175, 30, 0, 5, -10]
res1 = list(filter(lambda x: x % 5 == 0, data))
res2 = list(filter(lambda x: x % 10 == 5 or x % 3 == 0, data))
res3 = list(filter(lambda x: x % 5 == 0 and x % 3 == 0, data))
print(res1)
print(res2)
print(res3)


# # def filter(f, col): # вид функции 'filter' в программном коде
# #     return [x for x in col if f(x)] # возврат тех 'x' из списка 'col',
#                                       # которые прошли проверку условия f(x) 
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) 
# print(data)
# res = filter(lambda x: x % 2 == 0, res) 
# res = list(map(lambda x: (x, x**2), res))
# print(res)



# 00:26:20

""" Функция zip """
"""
Функция zip() применяется к набору итерируемых объектов 
и возвращает итератор с кортежами из элементов входных данных
"""

''' Пример: '''

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# ''' Функция zip () пробегает по минимальному входящему набору: '''

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]



# # 00:27:55

""" Функция enumerate """
"""
Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
кортежами из индекса и элементов входных данных.
Функция enumerate() позволяет пронумеровать набор данных. 
"""
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]



# # 00:28:40

""" Файлы """

'''
Файлы в текстовом формате используются для:
    ● Хранения данных
    ● Передачи данных в клиент-серверных проектах
    ● Хранения конфигов
    ● Логирования действий

Что нужно для работы с файлами:
    1. Завести переменную, которая будет связана с этим текстовым файлом.
    2. Указать путь к файлу.
    3. Указать, в каком режиме мы будем работать с файлом.
'''

# # 00:29:00
'''
Варианты режима (мод):

    a (apened) – открытие для добавления данных.
        ○ Позволяет дописывать что-то в имеющийся файл.
        ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
        и в него начнется запись.

    r (read) – открытие для чтения данных.
        ○ Позволяет читать данные из файла.
        ○ Если вы попробуете считать данные из файла, которого не существует, 
        программа выдаст ошибку.

    w – открытие для записи данных.
        ○ Позволяет записывать данные и создавать файл, если его не существует.
'''

'''
Миксованные режимы:

    1. w+
        ○ Позволяет открывать файл для записи и читать из него.
        ○ Если файла не существует, он будет создан.

    2. r+
        ○ Позволяет открывать файл для чтения и дописывать в него.
        ○ Если файла не существует, программа выдаст ошибку. 
'''

# 00:29:50

'''
Примеры использования различных режимов в коде:

1. Режим a (apened)
'''

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # 'a' - режим, в котором будем работать
#                              # (открытие для добавления данных)
# data.writelines(colors) # разделителей не будет
# data.close() # обязательное закрытие файла в конце

'''
    ● data.close() — используется для закрытия файла, 
      чтобы разорвать подключение файловой переменной с файлом на диске.
    ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
    ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
    ● При повторном выполнении скрипта redbluedreenredbluedreen 
      — добавление в существующий файл, а не перезапись файлов.
'''

# 00:31:00

''' 
Ещё один способ записи данных в файл: 
'''
# with open('file.txt', 'w') as data: # 'w' - режим записи данных 
#                                     # (полная перезапись данных в файле при каждом изменении)
#                                     # в случае отсутствия, файл будет создан
#     data.write('line 1\tline 01 ') # '\t' - одной строкой без переноса на новую строку
#     data.write('line 2\nline 3') # '\n' - перенос на новую строку


# # 00:32:20

''' 2. Режим r (read)

    ● Чтение данных из файла:
'''
# path = 'file.txt'
# data = open(path, 'r')  # переменную 'path' можно не задавать отдельно, 
#                         # сделав запись 'file.txt' внутри скобок 'open'
# for line in data:
#     print(line)
# data.close() # обязательное закрытие файла в конце


''' 3. Режим w '''

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

'''
    ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
    ● В случае перезаписи новые данные записываются, а старые удаляются.
'''


# 00:32:50

""" Модуль os """
'''
Модуль os предоставляет множество функций для работы с операционной системой, 
причем их поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою программу:
import os
Базовые функции данного модуля:
    ● os.chdir(path) - смена текущей директории. '''
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
''' 
    ● os.getcwd() - текущая рабочая директория 
'''
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'


""" 
    ● os.path - является вложенным модулем в модуль os 
    и реализует некоторые полезные функции для работы с путями, такие как:
    ○ os.path.basename(path) - базовое имя пути """
# import os 
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'
""" 
    ● os.path.abspath(path) - возвращает нормализованный абсолютный путь. 
"""
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

""" Это лишь малая часть возможностей модуля os. """


# 00:34:25

""" Модуль shutil """

'''
Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок. 
В частности, доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. 
Часто используется вместе с модулем os.

Для того, чтобы начать работать с данным модулем, необходимо его импортировать в свою программу:
'''
# import shutil

'''
Базовые функции данного модуля: '''

# shutil.copyfile(src, dst)   # копирует содержимое (но не метаданные) файла src в файл dst.
# shutil.copy(src, dst)       # копирует содержимое файла src в файл или папку dst.
# shutil.rmtree(path)         # Удаляет текущую директорию и все поддиректории; 
                            # path должен указывать на директорию, а не на символическую ссылку.

# 00:35:30

''' 
Итоги пройденного на лекции 4:

    ● Функции высшего порядка:
        ○ map
        ○ filter
        ○ zip
        ○ lambda
        ○ enumerate
    ● Работа с файлами
    ● Библиотеки для работы с операционной системой и файлами

P.S. Почитать документацию по работе с Pyhton
'''