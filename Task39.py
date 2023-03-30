# Даны два списка чисел. Требуется вывести те элементы первого списка , 
# которых нет во втором списке.
# Создайте функцию.
# Аргументы: два списка целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
# <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# from time import perf_counter

# def funk (list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return list(set1.difference(set2))

# def funk (list1, list2):
#     return list(set(list1).difference(set(list2)))

# print(funk([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))

# def funk2 (list1, list2):
#     new_list = list()
#     for i in list1:
#         if i not in list2 and i not in new_list:
#             new_list.append(i)
#     return new_list

# print(funk2([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))

from time import perf_counter
from random import randint


def funk_set(list1, list2):
    t1 = perf_counter()
    rez = list(set(list1).difference(set(list2)))
    t2 = perf_counter()
    return rez, t2 - t1


def funk_list(list1, list2):
    t1 = perf_counter()
    new_list = list()
    for i in list1:
        if i not in list2 and i not in new_list:
            new_list.append(i)
    t2 = perf_counter()
    return new_list, t2 - t1


n = 10000
lst1 = [randint(0, int(n)) for _ in range(n)]
lst2 = [randint(0, int(n)) for _ in range(n)]

print(funk_set(lst1, lst2)[1])
print(funk_list(lst1, lst2)[1])