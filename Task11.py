# Задача №11 Дано натуральное число А > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите число n, что f(n) = A. Если А не 
# является числоv Фибоначчи, выведите число -1.

# n = int(input("Введите число "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end = " ")
#     a, b = b, a
#     b += a

n = int(input("Введите число "))
a = 0
b = 1
counter = 1

if n == 0:
    print(counter)
else:
    while(a < n):
        a, b = b, a + b
        counter += 1
        print(a, counter)
    if n == a:
        print(f"Число на позиции {counter}")
    else:
        print("-1")