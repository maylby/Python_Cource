""" Хранилище модулей кодов """

""" Функция 'max1' (выбор максимального числа) """

def max1(a, b):
    if a > b: return a
    return b

""" Функция 'fib' (последовательность Фибоначчи) """

def fib(n):
    if n == 0: return 0
    if n in [1, 2]: return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(0, n):
    list_1.append(fib(i))
