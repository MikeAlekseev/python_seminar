# Пользователь вводит число N - общее количество
# рассматриваемых дней (1<=N<=100). В следующих строках
# располагается N целых чисел.
# Каждое число - среднесуточная температура в соответствующий день.
# Температуры - целые числа и лежат в диапозоне от -50 до 50

import random


days = input("Введите общее количество дней ")
temperature = list()
temp = 0
resultTemp = 0

for i in range(int(days)):
    temperature.append(random.randint(-50, 50))

for i in range(int(days)):
    if(int(temperature[i] > 0)):
        resultTemp += 1
    else:
        if(resultTemp > temp):
            temp = resultTemp
        resultTemp = 0
print(temperature)