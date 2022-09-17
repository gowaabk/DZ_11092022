"""

    Вычислить число c заданной точностью d

    Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
 """


def find_pi(num: int):
    n_pi = 0
    for i in range(0, num):
        n_pi += (1/(16**i))*((4/(8*i+1))-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
    return n_pi


n = input('Введите точность в формате x.xxxxx1 --> ')
num_len = len(n.split('.')[1])

template = '{:.' + str(num_len) + 'f}'

print(template.format(find_pi(num_len)))
