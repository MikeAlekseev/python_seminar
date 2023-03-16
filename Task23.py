# Задача 23: Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3]

import random

nums = input("Введите количество целых яисел")

array = [random.randint(-10, 10) for _ in range(int(nums))]
counter = 0
result_string = " "
print(array)

for i in range(len(array) - 1):
    if(array[i] < array[i + 1]):
        counter += 1
        result_string += f'{array[i]} < {array[i + 1]}'
        
print(f'{counter} ({result_string})')