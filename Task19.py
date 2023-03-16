# Задача 19: Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

array_length = input("Введите количество чисел ")
k = input("Введите сдвиг ")

nums_array = [i for i in range(1, int(array_length) + 1)]
print(nums_array)

for i in range(int(k)):
    nums_array.insert(0, nums_array.pop())

print(nums_array)