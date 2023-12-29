# Знакомство с языком Python (лекции)
# Урок 2. Коллекции данных. Профилирование и отладка
# https://gb.ru/lessons/391148


# 00:04:00

""" Списки """

# list_1 = [] # пустые квадратные скобки - значит открыт "список"
# list_1 = list() # список с указанием типа данных
# list_1 = [1, 2, 3, 8] # указание данных списка
# print(*list_1) # в отсутствие "*" список выводится в квадратных скобках
#                # "*" (звёздочка) удаляет квадратные скобки

# for i in list_1: # перебор списка циклом 'for'
#     print(i) # выведение 'i' при каждой итерации цикла
#              # 'i' будет принимать значения из списка
# print(len(list_1)) # функция "len" - проверка размера списка (количество элементов)
# print(list_1[0]) # обращение к конкретному элементу списка
#                  # отрицательное значение в скобках "[-1]" - вызов элементов с конца


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


# 00:09:00

''' Удаление конкретного элемента списка '''

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12 -> удаление нулевого элемента списка
# print(list_1) # [7, -1, 21, 0]


# 00:09:50

''' Добавление элемента на нужную позицию '''

# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# list_1.insert(2, 11) # первое число - позиция элемента, второе, сам элемент
# a = list_1.insert(2, 11) # передача значения переменной 'a'
# print(a) # 'None' - опосредованный вывод на экран
# print(list_1.insert(2, 11)) # 'None' - прямой вывод
# print(list_1) # [12, 7, 11, -1, 21, 0]
#               # [12, 7, 11, 11, 11, -1, 21, 0] - тройной повтор "insert"


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
# print(list_1[0:len(list_1):6]) # [1, 7] -> вывод от начала до конца, шаг 6 (шесть)
# print(list_1[::6]) # [1, 7] -> иной вариант записи того же самого


# 00:12:00

''' Кортежи '''

""" Кортеж - это неизменяемый список

Кортежи нужны для защиты каких-либо данных от изменений (намеренных или случайных). 
Кортеж занимает меньше места в памяти и работают быстрее, по сравнению со списками """

# t = () # создание пустого кортежа ('tuple')
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

# v = tuple(v) # смена типа данных на 'tuple' (кортеж)
# print(v) # (1, 8, 9) <- вывод значений в круглых скобках - признак кортежа
# print(type(v)) # тип данных изменён на class 'tuple' (кортеж)

# # a, b = 1, 2
# # a = b = 1
# a, b, c = v
# print(a,b,c)


""" Отличия и сходства кортежа и списка """

# t = (1, 2, 3, 5,)   # признак кортежа - наличие запятой после последнего элемента
#                     # при выводе, последняя запятая не печатается
# print(t, '->', type(t)) # одновременный вывод кортежа и типа данных
# t = list(t) # изменение типа данных с кортежа ('tuple') на список ('list')
# print(t, '->', type(t))
# t = [1, 2, 3, 5]
# print(t[1]) # вызов элемента по индексу
# print() # разрыв

# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2  # данная команда на замену значения элемента,
#           # применённая для кортежа,
#           # выдаст ошибку, т.к. кортежи нельзя изменять,
#           # предварительно нужно изменить тип данных
# print('t[0] =', t[0])
# print('t =', t)


# 00:18:25

''' Словари '''

''' Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
В списках в качестве ключа используется индекс элемента. 
В словаре для определения элемента используется значение ключа (строка, число).'''

# d = {} # открыть словарь, признак словаря - фигурные скобки
# d = dict() # открыть словарь с помощью оператора 'dict'

# d['q'] = 'qwerty' # ключ ('q') и значение ('qwerty')
# # print(d) # выдача по запросу "(d)" -> "{'q': 'qwerty'}"

# d['w'] = 'werty'
# print(d['q']) # выдача только значения по указанному ключу "d['q']" -> "qwerty"
# print(d) # выдача по запросу "(d)" 2-х ключей со значениями -> {'q': 'qwerty', 'w': 'werty'}
# print(d['q'], d['w']) # аналогичная выдача

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
                    # ключ в 'словаре' (Pyhton) заменяет индекс индекса
# print(dictionary['left']) # '←' - вывод на экран 
# print(dictionary['up']) # '↑' - вывод на экран 
                          #  типы ключей могут отличаться
# dictionary['left'] = '⇐' # замена выводимого по ключу значения
# print(dictionary['left']) # ⇐

# print(dictionary['type']) # KeyError: 'type' (ошибка ключа 'type' не существует)
# del dictionary['left'] # удаление элемента (функция 'del' и ключ, который хотим удалить)

# dictionary[89] = 98998 # добавление ключа '89' и значения "98998", соответствующего ключу
# print(dictionary) # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→', 89: 98998} 
#                   #  вывод словаря с добавлеными ключом и числом ('89: 98998')

# for item in dictionary: # перебор "словаря" циклом "for"
#     print('{}: {}'.format(item, dictionary[item])) # форма вызова "ключей" и их "значений" 
#                                                    # вывод в столбик каждой пары
#     print(item) # при использовании 'item' на экран выводятся, только "ключи"

# print(dictionary.items()) # вывод -> dict_items([('up', '↑'), ('down', '↓'), ('right', '→')])
#                           # выдача "словаря" в виде "списка" "кортежей", 
#                           # где указаны "ключ" и его "значение"

# for (k,v) in dictionary.items(): # перебор "ключей" и их "значений" (другая форма записи)
#                                  # 'k' - ключ, 'v' - значение
#                                  # буквы использованы для краткости, могут быть любыми
#                                  # можно написать слова, например, 'key', 'value'
#                                  # (!!!) числа использовать нельзя
#     print(k,v) # вывод столбиком ("ключи" и их "значения")
#     # up ↑
#     # left ← 
#     # down ↓
#     # right →


# 00:24:20

""" Множества """

""" Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
Одно множество может содержать значения любых типов. 
Если есть два множества, над ними можно совершать любые стандартные операции, 
например, объединение, пересечение и разность. Давайте разберем их."""

# colors = {'red', 'green', 'blue'} # в отличие от "словарей", 
#                                   # "множество" содержит, только перечень без "ключей"
# print(colors) # вывод -> {'red', 'green', 'blue'}
# colors.add('red') # "add" - # существующее значение ('red') добавить нельзя 
# print(colors) # вывод тот же -> {'red', 'green', 'blue'}
# colors.add('gray') # можно добавить, только новое значение, которого нет в перечне
# print(colors) # {'gray', 'red', 'green', 'blue'} 
#               # новое значение система добавляет в любое место перечня произвольно,
#               # чтобы упорядочить значения, следует использовать списки
# colors.remove('red') # 'remove' <- удаление указанного значения ('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' 
                       # повторный запрос на удаление 'red', выдаст ошибку
# colors.discard('red') # ok <- 'discard' проверяет наличие значения ('red'), 
#                       # если указанное значение существует, 
#                       # то 'discard' удаляет его, 
#                       # если нет, пропускает строку, 
#                       # не выдавая сообщения об ошибке.
# print(colors)
# colors.clear() # {} <- 'clear' удаляет всё множество
# print(colors) # set() <- выдача на экран

# q = set() # с помощью функции 'set' можно создавать любое множество


# 00:27:00

""" Операции со множествами в Python: """

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} <- "передача" значений множества "а" множеству "с"
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} <- "объединение", 
#                # выбор уникальных значений обоих множеств "a" и "b"
# i = a.intersection(b) # i = {8, 2, 5} <- "пересечение", 
#                       # выбор элементов, которые есть в обоих множествах
# dl = a.difference(b) # dl = {1, 3} <- "разность", 
#                      # вычитание из "а" совпадающих значений множества "b" (2, 5, 8)
# dr = b.difference(a) # dr = {13, 21} <- "разность", 
#                      # вычитание из "b" совпадающих значений множества "a" (2, 5, 8)
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
#                                              # находим "пересечение" ('intersection')
#                                              # множеств 'a', 'b' (последняя функция),
#                                              # затем "объединяем" ('union') и множества 'a', 'b',
#                                              # после чего "вычитаем" ('difference') 
#                                              # из "объединения" множеств "a" и "b" их "пересечение"


# 00:29:00

""" Неизменяемое или замороженное множество(frozenset) — 
множество, с которым не будут работать методы удаления и добавления."""

# a = {1, 2, 3, 5, 8} # некое множество "а"
# b = frozenset(a) # функция 'frozenset' замораживает множество "а" при его передаче "b"
#                  # "замороженное" множество нельзя изменять
# print(b) # вывод -> frozenset({1, 2, 3, 5, 8})


# 00:30:00

""" Коллекции данных 
    
№  Тип данных         | изменяемость  |  индексированность  |  уникальность   |   создаём
----------------------|---------------|---------------------|-----------------|--------------------
1. Список (list)      |    +          |        +            |      -          | [], list()
----------------------|---------------|---------------------|-----------------|--------------------
2. Кортеж (tuple)     |    -          |        +            |      -          | (), tuple()
----------------------|---------------|---------------------|-----------------|--------------------
3. Строка (string)    |    -          |        +            |      -          | '', ""
----------------------|---------------|---------------------|-----------------|--------------------
4. Множество (set)    |    +          |        -            |      +          | {elm1, elm2}, set()
----------------------|---------------|---------------------|-----------------|--------------------
5. Неизменное         |               |                     |                 |
множество (frozenset) |    -          |        -            |      +          | frozenset()
----------------------|---------------|---------------------|-----------------|--------------------
6. Словари (dict)     |    + элементы |        -            |      + элементы | {}
                      |    - ключи    |                     |      - ключи    | {key: value}
                      |    + значения |                     |      + значения | dict()
"""


# 00:31:50

""" List Comprehension («генератора списка») """

""" У каждого языка программирования есть свои особенности и преимущества. 
Одна из культовых фишек Python — list comprehension (редко переводится на русский, 
но можно использовать определение «генератора списка»). 
Comprehension легко читать, и их используют как начинающие, так и опытные разработчики. 
List comprehension — это упрощенный подход к созданию списка, который задействует цикл for, 
а также инструкции if-else для определения того, что в итоге окажется в финальном списке."""

''' 1. Простая ситуация — список:
'''
# list_1 = [exp for item in iterable] # 'exp' (некое значение) 
#                                     # 'for item' (для) 
#                                     # 'in iterable' - в некую коллекцию данных 
# print(list_1)

# ''' заменяет следующую запись: ''' 
# n = 5
# for i in range(n): # где 'none' - добавляемое значение
#                         # 'range' - цикл добавлений
#                         # 'n' - число повторов
#     list(i) = none # 'none' - добавляемое значение
#     print(list_1)

    
''' 2. Выборка по заданному условию:
'''
# list_1 = [exp for item in iterable (if conditional)] # 'if conditional' - какое-то условие


# 00:33:00

''' Задача '''
""" Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
Решение:
"""
# list_01 = []
# for i in range(1, 11):
#     list_01.append(i) # VSCode сообщает об ошибке в данной строке
# print(list_01) # [1, 2, 3,..., 10]


""" Эту же функцию можно записать так:
"""
list_02 = [i for i in range(1, 11)] # вывод списка -> [1, 2, 3,..., 10]
                                    # смысл записи:
                                    # значение 'i'
                                    # циклом 'for'
                                    # выбрать ('range')
                                    # из промежутка от 1 до 11
print(list_02)



""" Задача """
""" 2. Добавить, (условие) только чётные числа """

list_1 = [i for i in range(1, 11) if i % 2 == 0]  # вывод -> [2, 4, 6, 8, 10]
                                                  # выбрать числа из промежутка от 1 до 11
                                                  # при условии выбора ('if')
                                                  # только чётных значений ('i % 2 == 0')
print(list_1) 


""" Создание пары каждому из чисел (кортежи) """

list_21 = [(i, i) for i in range(1, 11) if i % 2 == 0]  # [(2, 2), (4, 4),..., (10, 10)]
                                                        # список кортежей (i, i)
                                                        # из пар одинаковых чётных чисел

list_22 = [(i, i*i) for i in range(1, 9) if i % 2 == 0] # [(2, 4), (4, 16), (6, 36), (8, 64)]
                                                        # список кортежей (i, i*i)
                                                        # из пар чётного числа и его квадрата
                                                        # в промежутке от 1 до 9
print(list_21)
print(list_22)


""" Также можно умножать, делить, прибавлять, вычитать. 
Например, умножить значение на 2. """

list_3 = [i * 2 for i in range(10) if i % 2 == 0] # список произведений ('i*2')
                                                  # чётных чисел ('i % 2 == 0')
                                                  # из первого натурального десятка ('range(10)')
print(list_3) # [0, 4, 8, 12, 16]


# 00:34:45

""" Профилирование и отладка
Мы с вами люди, а людям свойственно ошибаться, даже при написании программного кода
Давайте разберем с Вами самые частые ошибки в написании кода на Python.
🔥Самые распространенные ошибки:
○ SyntaxError(Синтаксическая ошибка) """

# number_first = 4
# number_second = 5
# if number_first > number_second # <- Отсутствие двоеточия (':') после цикла
#     print(number_first)
# else: print('First number less than second')


''' ● IndentationError (Ошибка отступов) '''

# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # <- Отсутствие отступов


''' ● TypeError (Типовая ошибка) '''

# text = 'Python'
# number = 5 # следует взять число в кавычки ('5'), превратив его в строку
# print(text + number) # <- ошибочная запись (сложение строки и числа)


''' ● ZeroDivisionError (Деление на 0) '''

# number_first = 5
# number_second = 0
# print(number_first // number_second) # Делить на ноль нельзя


''' ● KeyError (Ошибка ключа) '''

# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3]) # Такого ключа не существует


''' ● NameError(Ошибка имени переменной) '''
# name = 'Ivan'
# print(names) # Переменной 'names' не существует


''' ● ValueError(Ошибка значения) '''

# text = 'Python' # слово 'Python' следует заменить набором чисел ('555')
# print(int(text)) # Нельзя символы перевести в целые значения
