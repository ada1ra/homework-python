def is_valid_recursive(board, row, col):
    # проверяем, можно ли поставить ферзя на позицию (row, col)
    for i in range(row):
        # проверка столбца и диагоналей
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_recursive(n, row, board, solutions):
    # рекурсивно находит все решения
    if row == n:
        solutions.append(board)
        return

    for col in range(n):
        if is_valid_recursive(board, row, col):
            board[row] = col
            # возвращаемся к 1 строке и смотрим следующий столбец
            solve_recursive(n, row + 1, board, solutions)

def queens_recursive(n):
    # запускаем решение
    if n < 1:
        return 0

    solutions = []
    board = [-1] * n  # board[i] = столбец ферзя в строке i
    solve_recursive(n, 0, board, solutions)
    return len(solutions)

# тест
for n in range(1, 11):
    print(f"n={n}: {queens_recursive(n)} решений")
