# У вас есть монеты номиналом в длина имени, длина фамилии, длина отчества(если нет, то 19).
# Напишите программу, выписывающую размен считанного с консоли числа, если таковой возможен.
# В противном случае выведите "-42!".
# 3, 10, 8

COIN_1 = 10  # номинал 1-ой монеты
COIN_2 = 8   # номинал 2-ой монеты
COIN_3 = 3   # номинал 3-ей монеты
take = ''   # число для размена, взятое через input
test = 0    # переменная-флаг для проверки правильности введённого формата

# проверка правильности введённого формата
while test == 0:
    try:
        take = int(input('Введите число для размена: '))
        test = 1
    except ValueError:
        print('Неверный формат!')


def change(x=0, y=take, z=[0, 0, 0]):
    global COIN_1, COIN_2, COIN_3

    if x == y:
        return z  # нашли решение, возвращаем его

    if x > y:
        return None  # превышение суммы, нет решения

    # пробуем добавить монету COIN_1
    res = change(x + COIN_1, y, [z[0] + 1, z[1], z[2]])
    if res is not None:
        return res

    # пробуем добавить монету COIN_2
    res = change(x + COIN_2, y, [z[0], z[1] + 1, z[2]])
    if res is not None:
        return res

    # пробуем добавить монету COIN_3
    res = change(x + COIN_3, y, [z[0], z[1], z[2] + 1])
    if res is not None:
        return res

    return None  # решений нет


result = change()

if result is None:
    print('-42!')
else:
    print(f'{result[0]} монет по {COIN_1}, {result[1]} монет по {COIN_2} и {result[2]} монет по {COIN_3}.')
