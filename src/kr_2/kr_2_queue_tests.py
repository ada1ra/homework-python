"""
Запуск: pytest kr_2_queue_tests.py -v
"""
import pytest
from kr_2_queue import BinomialHeap, BinomialNode

class TestBasicOperations:
    """Проверка базовых операций вставки, поиска и извлечения минимума"""
    def test_empty_heap(self):
        """Проверка пустой кучи"""
        heap = BinomialHeap()
        assert heap.is_empty() == True
        assert heap.get_minimum() is None
        assert heap.extract_min() is None

    def test_single_insert(self):
        """Вставка одного элемента"""
        heap = BinomialHeap()
        heap.insert(10, "A")

        assert heap.is_empty() == False
        min_node = heap.get_minimum()
        assert min_node.key == 10
        assert min_node.value == "A"

    def test_multiple_inserts(self):
        """Вставка нескольких элементов"""
        heap = BinomialHeap()
        heap.insert(10, "A")
        heap.insert(5, "B")
        heap.insert(20, "C")
        heap.insert(3, "D")
        heap.insert(7, "E")

        # проверка поиска минимума
        min_node = heap.get_minimum()
        assert min_node.key == 3
        assert min_node.value == "D"

        # проверка извлечения минимума
        extracted = heap.extract_min()
        assert extracted.key == 3
        assert extracted.value == "D"

        # проверка нового минимума
        min_node = heap.get_minimum()
        assert min_node.key == 5
        assert min_node.value == "B"
