def backtrack(row, columns, diagonal1, diagonal2):
    if row == n:
        return 1

    count = 0
    for col in range(n):
        # вычисляем номера диагоналей
        d1 = row - col  # диагональ \
        d2 = row + col  # диагональ /

        # проверяем конфликты
        if col in columns or d1 in diagonal1 or d2 in diagonal2:
            continue

        # добавляем ферзя
        columns.add(col)
        diagonal1.add(d1)
        diagonal2.add(d2)

        # рекурсивный вызов
        count += backtrack(row + 1, columns, diagonal1, diagonal2)

        # убираем ферзя (откат)
        columns.remove(col)
        diagonal1.remove(d1)
        diagonal2.remove(d2)

    return count


def queens_simple(n):
    # рекурсивное решение с множествами
    if n < 1:
        return 0

    return backtrack(0, set(), set(), set())


# тест
for n in range(1, 11):
    print(f"n={n}: {queens_simple(n)} решений")
