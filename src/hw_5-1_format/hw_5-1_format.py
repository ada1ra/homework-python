# У вас есть монеты номиналом в длина имени, длина фамилии, длина отчества(если нет, то 19).
# Напишите программу, выписывающую размен считанного с консоли числа, если таковой возможен.
# В противном случае выведите "-42!".
# 3, 10, 8

coin1 = 10  # номинал 1-ой монеты
coin2 = 8   # номинал 2-ой монеты
coin3 = 3   # номинал 3-ей монеты
take = ''   # число для размена, взятое через input
test = 0    # переменная-флаг для проверки правильности введённого формата

# проверка правильности введённого формата
while test == 0:
    try:
        take = int(input('Введите число для размена: '))
        test = 1
    except:
        print('Неверный формат!')

def change(x=0, y=take, z=[0, 0, 0]):
    global coin1, coin2, coin3

    if x == y:
        return z  # нашли решение, возвращаем его

    if x > y:
        return None  # превышение суммы, нет решения

    # пробуем добавить монету coin1
    res = change(x + coin1, y, [z[0] + 1, z[1], z[2]])
    if res is not None:
        return res

    # пробуем добавить монету coin2
    res = change(x + coin2, y, [z[0], z[1] + 1, z[2]])
    if res is not None:
        return res

    # пробуем добавить монету coin3
    res = change(x + coin3, y, [z[0], z[1], z[2] + 1])
    if res is not None:
        return res

    return None  # решений нет

result = change()

if result is None:
    print('-42!')
else:
    print(f'{result[0]} монет по {coin1}, {result[1]} монет по {coin2} и {result[2]} монет по {coin3}.')
