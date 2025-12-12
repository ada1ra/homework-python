class BinomialNode:
    """Узел биномиального дерева"""
    def __init__(self, key, value=None):
        self.key = key  # приоритет (меньше = выше приоритет)
        self.value = value  # данные, хранимые в узле
        self.degree = 0  # степень узла(количество детей)
        self.parent = None  # родительский узел
        self.child = None  # указатель на крайнего левого ребенка
        self.sibling = None # указатель на правого брата

class BinomialHeap:
    """Биномиальная куча (очередь с приоритетами)"""
    def __init__(self):
        self.head = None  # голова списка корней

    def is_empty(self):
        """Проверка на пустоту"""
        return self.head is None


    def insert(self, key, value=None):
        """Вставка элемента в кучу"""
        # создаем новую кучу из одного элемента
        node = BinomialNode(key, value)
        new_heap = BinomialHeap()
        new_heap.head = node

        # сливаем с текущей кучей
        self._union(new_heap)

    def get_minimum(self):
        """Поиск минимального элемента"""
        if self.head is None:
            return None

        min_node = self.head
        current = self.head.sibling

        while current:
            if current.key < min_node.key:
                min_node = current
            current = current.sibling

        return min_node

    def _union(self, other_heap):
        """Слияние двух биномиальных куч"""
        merged_head = self._merge_root_lists(self.head, other_heap.head)

        if merged_head is None:
            self.head = None
            return

        prev = None
        x = merged_head
        next_node = x.sibling

        while next_node:
            # степени разные или три дерева подряд одинаковой степени
            if x.degree != next_node.degree or (next_node.sibling == x.degree and next_node.sibling.degree == x.degree):
                prev = x
                x = next_node
            else:
                if x.key <= next_node.key:
                    x.sibling = next_node.sibling
                    self._link_trees(next_node, x)
                else:
                    if prev is None:
                        merged_head = next_node
                    else:
                        prev.sibling = next_node
                    self._link_trees(x, next_node)
                    x = next_node

            next_node = x.sibling
        self.head = merged_head

    def _merge_root_lists(self, head_1, head_2):
        """Слияние двух списков корней в один отсортированный по степени"""
        temp = BinomialNode(0)
        tail = temp

        while head_1 and head_2:
            if head_1.degree <= head_2.degree:
                tail.sibling = head_1
                head_1 = head_1.sibling
            else:
                tail.sibling = head_2
                head_2 = head_2.sibling
            tail = tail.sibling

        if head_1:
            tail.sibling = head_1
        else:
            tail.sibling = head_2

    def _link_trees(self, child, parent):
        """Связывание двух деревьев одинаковой степени"""
        child.parent = parent
        child.sibling = parent.child
        parent.child = child
        parent.degree += 1

    def extract_min(self):
        """Извлечение узла с минимальным значением ключа"""
        if self.head is None:
            return None

        min_node = self.head
        min_prev = None
        prev = None
        current = self.head

        while current:
            if current.key < min_node.key:
                min_node = current
                min_prev = prev
            prev = current
            current = current.sibling

        if min_prev is None:
            self.head = min_node.sibling
        else:
            min_prev.sibling = min_node.sibling

        child_head = None
        child = min_node.child
        while child:
            next_child = child.sibling
            child.sibling = child_head
            child.parent = None
            child_head = child
            child = next_child

        child_heap = BinomialHeap()
        child_heap.head = child_head
        self._union(child_heap)
        return min_node


    def decrease(self, node, value):
        """Уменьшает ключ элемента, присваивая новое значение"""
        if value > node.key:
            return
        node.key = value
        parent = node.parent
        while parent and node.key < parent.key:
            node.key, parent.key = parent.key, node.key
            node.value, parent.value = parent.value, node.value

            node = parent
            parent = node.parent

    def delete(self, node):
        """Удаление ключа"""
        decrease(self, node, -10**9)
        extract_min(self)
