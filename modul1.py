""" Хранилище модулей кодов """

""" Функция 'max1' (выбор максимального числа) """

def max1(a, b):
    if a > b: return a
    return b


def min1(a, b):
    if a < b: return a
    return b


def guick_sort(array):

    if len(array) <= 1: return array
    else: pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return guick_sort(less) + [pivot] + guick_sort(greater)


def guick_sort_back(array):

    if len(array) <= 1: return array
    else: pivot = array[0]

    less = [i for i in array[1:] if i > pivot]
    greater = [i for i in array[1:] if i <= pivot]
    return guick_sort_back(less) + [pivot] + guick_sort_back(greater)