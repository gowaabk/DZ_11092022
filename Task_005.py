""" Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
 """


import re


def in_mnogo(file_name):  # функция чтения из файла
    f = open(file_name, 'r')
    list1 = f.read()
    f.close()
    return list1


# Формирует сумму многочленов в виде строки
def func_mnogo(list_mnogo: list, num: int):
    mnogo = ''
    for i in range(len(list_mnogo)-1, 0, -1):
        q = list_mnogo[-i-1]
        if q != 0:
            mnogo += f'{q}*x^{i} + '
        w = list_mnogo[-1]
        if w == 0:
            return mnogo[:-3]+' = 0'
    return mnogo+f'{w} = 0'


def summ_mnogo4(mnogo1_norm: list, mnogo2_norm: list):
    sum_mnogo = []
    for i in range(0, len(mnogo1_norm), 3):
        sum_mnogo.append(int(mnogo1_norm[i])+int(mnogo2_norm[i]))
    return sum_mnogo


mnogo1 = in_mnogo('mnogo1.txt')[:-2]
mnogo2 = in_mnogo('mnogo2.txt')[:-2]
print(f'1-ый многочлен - {mnogo1}')
print(f'2-ой многочлен - {mnogo2}')

mnogo1_norm = (re.split('[*|^|+|' ']', mnogo1))
mnogo2_norm = (re.split('[*|^|+|' ']', mnogo2))
# print(mnogo1_norm)
# print(mnogo2_norm)
sum_mnogo = summ_mnogo4(mnogo1_norm, mnogo2_norm)
print(f'Сумма коэфф-в многочленов - {sum_mnogo}')
print(f'Сумма двух многочленов - {func_mnogo(sum_mnogo, len(sum_mnogo))}')
