""" Задайте последовательность чисел.
Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности. """

import random


def create_random_list(list2: list, width: int):  # Функция генерации списка
    for i in range(width):
        list2.append(random.randint(0, width))
    return list2


def find_uniq_num(in_list: list):
    out_list = []
    for i in in_list:
        if in_list.count(i) == 1:
            out_list.append(i)
    return out_list


n = 8
gen_list = []

create_random_list(gen_list, n)
print(f'Сгенерированный список: {gen_list}')

new_list = find_uniq_num(gen_list)
print(f"Список из неповторяющихся элементов: {new_list}")
