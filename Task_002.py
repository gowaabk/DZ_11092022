""" Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N. """


def prim_factors(num: int):
    i = 2
    prim_list = []
    while i * i <= num:
        while num % i == 0:
            prim_list.append(i)
            num = num / i
        i = i + 1
    if num > 1:
        prim_list.append(num)
    return prim_list


n = int(input('Введите число N --> '))
print(f'Простые множители числа {n} {prim_factors(n)}')
