# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3
#     <function_name>(10,34) -> 44


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def recurse(a, b):
    if a == 0 and b == 0:
        return 0
    if a != 0:
        return recurse(a - 1, b) + 1
    return recurse(a, b - 1) + 1
print(recurse(a, b))