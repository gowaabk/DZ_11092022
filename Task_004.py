"""     Задана натуральная степень k.
    Сформировать случайным образом список коэффициентов
    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

    Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 
степень уменьшается на 1
к = 2 - количество членов с Х"""

import random


def rand_koeff():   # Фомирует случайные коэффициенты
    return random.randint(0, 100)


def func_mnogo(num: int):  # Формирует многочлен в виде строки с k - количеством членов X
    mnogo = ''
    for i in range(num, 0, -1):
        q = rand_koeff()
        if q != 0:
            mnogo += f'{q}*x^{i} + '
        w = rand_koeff()
        if w == 0:
            return mnogo[:-3]+' = 0'
    return mnogo+f'{w} = 0'


def in_mnogo(list1: str):  # функция записи в файл
    f = open('file.txt', 'w')
    f.write(list1)
    f.close()
    return


k = int(input('Введите k --> '))
#k = 5
list_mnogo = func_mnogo(k)
print(list_mnogo)
in_mnogo(list_mnogo)
