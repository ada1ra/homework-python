# преобразование в двоичную кучу с корнем i (индекс в arr); n - размер кучи
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left
    r = 2 * i + 2  # right

    # проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l

    # проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # заменяем корень, если нашёлся элемент больше
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # применяем heapify к корню
        heapify(arr, n, largest)


# сортировка массива (основная функция)
def heap_sort(arr):
    n = len(arr)

    # строим max-heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # переворачиваем массив
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # свап
        heapify(arr, i, 0)

    return arr

#
# data = []
# n = int(input('Введите количество элементов: '))
#
# print(f'Введите {n} элементов')
# for i in range(n):
#     try:
#         current = int(input())
#     except ValueError:
#         print("Wrong input!")
#         current = int(input())
#
#     data.append(current)
#
# heap_sort(data)
# print(data)
