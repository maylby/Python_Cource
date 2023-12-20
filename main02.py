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