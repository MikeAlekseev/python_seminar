# Напишите рекурсивную функцию для возведения числа a в степень b
# Разрешается использовать только операцию умножения. 
# Циклы использовать нельзя
# Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def degree(a, b):
    if b == 0:
        return 1
    return degree(a, b - 1) * a
print(degree(a, b)) 