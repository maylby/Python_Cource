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

list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
