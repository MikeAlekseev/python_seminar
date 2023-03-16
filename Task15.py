# Пользователь вводит одно число N - количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число - это масса соответствующего арбуза.

import random

n = input("введите колво арбузов")
melon_weight = list()

for i in range(int(n)):
    melon_weight.append(random.randint(1, 10))

print(melon_weight)

min = melon_weight[0]
max = melon_weight[0]

for i in range(int(n)):
    if (melon_weight[i] < min):
        min = melon_weight[i]
    if (melon_weight[i] > max):
        max = melon_weight[i]
print("min = ", min)
print("max = ", max)