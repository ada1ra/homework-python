from hw_6_1_sort_with_test import heap_sort
from random import randint, uniform
import pytest

"""Обычные тесты"""


@pytest.mark.parametrize(
    ["n"], [(([randint(0, 300) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_positive(n):
    """Тест с неотрицательными числами"""
    assert heap_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([randint(-300, -1) for _ in range(10)]),) for _ in range(10)]
)
def test_heap_sort_negative(n):
    """Тест с отрицательными числами"""
    assert heap_sort(n) == sorted(n)


@pytest.mark.parametrize(
    ["n"], [(([uniform(-50, 50) for _ in range(10)]),) for _ in range(10)]
)
def test_float_numbers(n):
    """Тест с числами с плавающей точкой"""
    assert heap_sort(n) == sorted(n)


"""Тесты крайних случаев"""


def test_empty_list():
    """Тест пустого списка"""
    assert heap_sort([]) == []


def test_single_element():
    """Тест одного элемента"""
    assert heap_sort([5]) == [5]


def test_large_random_list():
    """Тест большого случайного списка"""
    test_list = [randint(-1000, 1000) for _ in range(1000)]
    assert heap_sort(test_list) == sorted(test_list)


def test_very_large_numbers():
    """Тест с очень большими числами"""
    assert heap_sort([2 ** 100, 0, -1, -2 ** 11]) == [-2 ** 11, -1, 0, 2 ** 100]


def test_already_sorted():
    """Тест уже отсортированного массива"""
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Тест с дубликатами"""
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


"""Некоторые сортировки для сравнения"""


def bubble_sort(arr):
    """Пузырьковая сортировка для сравнения"""
    if not arr:
        return arr.copy()
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(arr):
    """Сортировка выбором для сравнения"""
    if not arr:
        return arr.copy()
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


"""Сравнение с другими сортировками"""


def test_heap_sort_builtin():
    """Сравнение с встроенной сортировкой"""
    n = [1, 2, 10, 1, 100]
    assert heap_sort(n) == sorted(n)


def test_compare_with_bubble_sort():
    """Сравнение с пузырьковой сортировкой"""
    n = [1, 2, 10, 1, 100]

    assert heap_sort(n) == bubble_sort(n)


def test_compare_with_selection_sort():
    """Сравнение с сортировкой выбором"""
    n = [1, 2, 10, 1, 100]
    assert heap_sort(n) == selection_sort(n)
