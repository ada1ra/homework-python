import itertools

def is_valid_bruteforce(board):
    # проверяет, можно ли так поставить ферзей
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # проверка на одну диагональ
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True

def queens_bruteforce(n):
    # перебор всех возможных расстановок
    if n < 1 or n > 10:  # ограничение из-за сложности
        return 0

    count = 0
    # генерируем все перестановки (каждый ферзь в уникальной строке и столбце)
    for permutation in itertools.permutations(range(n)):
        if is_valid_bruteforce(permutation):
            count += 1
    return count


# тест
for n in range(1, 11):
    print(f"n={n}: {queens_bruteforce(n)} решений")
