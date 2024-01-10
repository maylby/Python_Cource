# Знакомство с языком Python (лекции)
# Урок 3. Функции, рекурсия, алгоритмы
# https://gb.ru/lessons/391149

"""
Содержание лекции 3

    ? Функции
    ? Модули
    ? Рекурсия
    ? Быстрая сортировка
    ? Сортировка слиянием
"""


""" Функции """
"""
Функция — это фрагмент программы, используемый многократно.
Мы знакомы уже с функциями в C#, давайте теперь посмотрим, как
создаются и используются функции внутри Python 

P.S. 
В Python не выделяются функции и процедуры, как 
самостоятельные единицы, они объединены в одно понятие "функция",
обозначаемую как "def".
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
# def sum_numbers(n, y = 'Hello'):  # 'sum_numbers' - имя функции
#                                   # 'def' - параметр, сообщающий, что задана функция
#                                   # тип данных указывать не нужно, т.к.
#                                   # у Pyhton динамическая типизация
#     print(y) # вывод данных на экран (в печать)
               
#     summa = 0 # создание переменной 'summa', с текущим значением равным нулю
#     for i in range(1, n+1): # цикл перебора чисел в промежутке от 1 до n+1
#         summa += i # увеличение значения переменной (summa), на значение индекса (i),
#                    # дающее последовательное сложение всех чисел промежутка (1, n+1)
#     # print(summa) # вывод результата суммирования
#                    # оператор вывода (print) можно заменить оператором возврата (return)
#     return summa # возврат (return) суммы, вместо её вывода (print)
#                  # при появлении оператора 'return', программа завершает работу
# print(n)
# print(sum_numbers(n))   # вызов функции (sum_numbers)
#                         # вывывод (print) данных на экран,
#                         # либо с указанием конкретного значения 'n', например, (5),
#                         # либо с указанием символа переменной (n),
#                         # если её значение было задано вначале (n = 5), как в данном случае
# a = sum_numbers(n, 'qwerty') # создание переменной 'a' 
#                              # и передача ей значения функции 'sum_numbers(n)',
#                              # а так же изменённые аргументы ('qwerty') параметра 'y'
# print(a) # вывод значения переменной 'a'



# 00:07:30

""" Функция принимающая любое кодичество аргументов """

# def sum_str(*args): # звёздочка '*' позволяет передавать неограниченное число аргументов
#                     # Какой в этом практический смысл?
#                     # Где и для чего можно применить эту функцию?
#     res = '' # строка для записи результата
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','l')) # выдача -> qel 
# print(sum_str('q','e','l','r','f')) # выдача -> qelrf
# # print(sum_str(a, s, d, f)) # передача открытых, не заковыченных знаков, выдаст ошибку
#                            #  Pyhton воспринимает их, как переменные
# # print(sum_str(1, 3, 4)) # передача открытых числовых значений, тоже выдаст ошибку
#                         # Pyhton интерпретирует их, как числа,
#                           # в то время как запись (res = '') сообщила, что задана строка
# print(sum_str('1', '3', '4')) # выдача -> 134
#                               # передача чисел в кавычках допустима, ошибки не возникает,
#                               # Pyhton читает их как строку


# 00:09:20

""" Модульность """
"""
Как работает, например, функция .append?
Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем.
Однако эта функция срабатывает автоматически, и чтобы ей пользоваться 
ничего дополнительно писать не надо, т.к. она уже внесена в базу данных Pyhton, 
откуда её можно вызвать, указав имя (.append).

Представим огромный проект, где имеется большое количество функций, 
к примеру 5 функций работают со словарями, 18 со списками и тд., 
и у каждой функции свой алгоритм, но все они объединены работой с одной коллекцией данных. 
Согласитесь, неудобно работать в таком большом файле, где около 80 функций, 
очень легко потеряться и на перемотку кода будет уходить драгоценное время. 
Решенить проблему можно, создав отдельные файлы, где будут находиться только функции, 
которые при необходимости можно будет вызывать из главного файла.
Файлы хранения можно подразделить по типу функций. Например: 
    1) функции по спискам, 
    2) по кортежам, 
    3) по словарям.
"""

''' 
Код размещён в файл "modul1.py" 
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
(импорт модуля)
'''
# a = input('input A: ', ) # ввод данных переменной (a) с клавиатуры
# b = input('input B: ', ) # ввод данных переменной (b) с клавиатуры
#                          # значения можно задавать непосредственно в коде, 
#                          # вводя их в 'modul1.max1', вместо (a, b)

# import modul1 # импорт модуля (modul1) для вызова функции
# print(modul1.max1(a, b)) # вывод результата работы выбранной функции "max1"

'''
Способ 2 
(импорт конкретной функции)
'''
# from modul1 import max1 # обращение к файлу (modul1)
#                         # указание импорта конкретной функции (max1) 
# print(max1(a, b)) # в этом случае, указывать файл хранения (modul1) не нужно
#                   # использован ввод данных (a, b) с клавиатуры (см. выше)

# from modul1 import * # звёздочка - это способ "импорта" всех "функций",
#                      # размещённых в указанном файле хранения (modul1)
# print(min1(a, b)) # вывод результата работы функции "min1" из "modul1"
# print(max1(a, b)) # вывод результата работы функции "max1" из "modul1"


# import modul1 as m1 # изменение имени файла "modul1" на "m1", 
#                     # 'm1' - временное имя для текущего использования
# print(m1.max1(a, b)) # в выводе (print) указываем файл хранения, 
#                      # используя имя "m1", вместо "modul1"


# 00:14:35

''' Рекурсия '''
'''
Рекурсия — это функция, вызывающая сама себя.
С рекурсией Вы знакомы с C#, в Python она ничем не отличается. 

Рассмотрим следующую задачу: 
Пользователь вводит число n. 
Необходимо вывести n - первых членов последовательности Фибоначчи.
Напоминание: Последовательно Фибоначчи, это такая последовательность, 
в которой каждое последующее число равно сумме 2-х предыдущих.
При описании рекурсии важно указать, когда функции надо остановиться и
перестать вызывать саму себя. Иначе говоря, необходимо указать базис рекурсии 
'''

''' Последовательность Фибоначчи '''

# n = int(input('input N: ', )) # ввод конечного числа последовательности
# def fib(n):
#     if n == 0: return 0 # возврат (0) - значение числа с индексом 0
#     if n in [1, 2]: return 1 # возврат (1) - значение чисел с индексами 1 и 2
#     return fib(n-1) + fib(n-2) # возврат последовательности Фибоначчи

# list_1 = [] # список "list_1" для записи последовательности чисел
# for i in range(0, n): # цикл перебора значений от 0 до n
#     list_1.append(fib(i)) # "append" - добавление каждого полученного значения 
#                           # в конец текущего списка (слева направо)
# print(list_1)


# 00:17:55

""" Алгоритмы """
"""
Алгоритмом называется набор инструкций для выполнения некоторой задачи. 
В принципе, любой фрагмент программного кода можно назвать алгоритмом, 
но мы с рассмотрим 2 самых интересных алгоритма сортировок:

● Быстрая сортировка
● Сортировка слиянием
"""

""" Быстрая сортировка """
"""
“Программирование это разбиение 
чего-то большого и невозможного на что-то маленькое и вполне реальное”.
Быстрая сортировка принадлежит такой стратегии, как “разделяй и властвуй”. 

Рассмотрим пример и напишем программный код.

Два друга решили поиграть в игру: 
один загадывает число от 1 до 100, другой должен отгадать.
Согласитесь, что мы можем перебирать эти значения в случайном порядке, 
например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, 
но что если мы обратиться к стратегии “разделяй и властвуй”. 
Обозначим друзей, друг_1 - это Иван, который загадал число, 
друг_2 - это Петр, который отгадывает. 
"""

# def guick_sort(array):

#     if len(array) <= 1: return array
#     else: pivot = array[0]

#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return guick_sort(less) + [pivot] + guick_sort(greater)

# print(guick_sort([10, 5, 2]))


""" Пояснение решения """
"""
● 1-е повторение рекурсии:
    ○ array = [10, 5, 2, 3]
    ○ pivot = 10
    ○ less = [5, 2, 3]
    ○ greater = []
    ○ return quicksort([5, 2, 3]) + [10] + quicksort([])

● 2-е повторение рекурсии:
    ○ array = [5, 2, 3]
    ○ pivot = 5
    ○ less = [2, 3]
    ○ greater = []
    ○ return quicksort([2, 3]) + [5] + quicksort([]) 
    # Важно! Здесь помимо вызова рекурсии добавляется список [10]

● 3-е повторение рекурсии:
    ○ array = [2, 3]
    ○ return [2, 3] # Сработал базовый случай рекурсии
    На этом работа рекурсии завершилась 
    и итоговый список будет выглядеть таким образом: 
    [2, 3] + [5] + [10] = [2, 3, 5, 10]
"""

# 00:27:00

""" Сортировка слиянием """

# def merge_sort(nums): # "merge" - слить (сортировка слиянием)
#     if len(nums) > 1: # условие продолжения (завершения): 
#                       # если длина списка больше 1, деаем то, что ниже
#         mid = len(nums) // 2 # "mid" - переменная, в которой будут храниться значения
#                              # "//" - делим спискок пополам и берём, только целую часть
#         left = nums[:mid] # список "left" - срез от начала до середины
#         right = nums[mid:] # список "right" - срез от середины до конца
#         merge_sort(left) # рекурсия для левой части, 
#                          # делящая списки пополам до последнего элемента
#         merge_sort(right) # рекурсия для правой части, делящая списки пополам
#         i = j = k = 0 # соединение всех элементов воедино
#                       # i - индекс (левый список), j - правый, k - итоговый
#                       # начальное значение трёх переменных (i, j, k) равно нулю
#         while i < len(left) and j < len(right): # - пока i меньше длины левого списка
#                                                 # - и (and) пока j меньше длины правого
#                                                 # "and" означает, что цикл будет завершён,
#                                                 # когда опустеет какой-либо из списков
#             if left[i] < right[j]: # если элемент слева меньше элемента справа,
#                 nums[k] = left[i] # присваиваиваем итоговому элементу значение левого
#                 i += 1 # увеличиваем индекс (i) на 1
#             else:
#                 nums[k] = right[j] # иначе, итоговому элементу присваиваем значение правого
#                 j += 1 # увеличиваем индекс (j) на 1, после чего
#             k += 1  # итоговый индекс (k) увеличиваем на 1
#                     # для перехода к новому значению на каждой следующей итерации
#         while i < len(left): # проверка остатка элементов в левом списке
#             nums[k] = left[i] # запись остатка в конец итогового списка 
#             i += 1 # переход к следующему значению (элементу)
#             k += 1 # обновление итогового списка для следующей итерации
#         while j < len(right): # проверка остатка элементов в правом списке
#             nums[k] = right[j] # запись остатка в конец итогового списка 
#             j += 1 # переход к следующему значению (элементу)
#             k += 1 # обновление итогового списка для следующей итерации
# list1 = [1,4,9,7,2,1,44,55,3,6] # заданный список
# merge_sort(list1) # передача функции значений списка "list1"
# print(list1) # вывод отсортированного списка