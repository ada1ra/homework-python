class Graph:

    # МЕТОДЫ СОЗДАНИЯ ГРАФА

    def __init__(self):
        """Инициализация неориентированного графа"""
        self.connections_list = {}

    def add_vertex(self, vertex):
        """Добавление вершины в граф"""
        if vertex not in self.connections_list:
            self.connections_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавление ребра"""
        # добавляем вершины, если их нет
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # добавляем связи в обе стороны
        if vertex2 not in self.connections_list[vertex1]:
            self.connections_list[vertex1].append(vertex2)
        if vertex1 not in self.connections_list[vertex2]:
            self.connections_list[vertex2].append(vertex1)

    # РЕАЛИЗАЦИЯ ПРОТОКОЛОВ ИНТЕРФЕЙСОВ

    def __iter__(self):
        """Делает граф итерируемым"""
        self._dfs_order = self.dfs()
        self._index = 0
        return self

    def __next__(self):
        """Возвращает следующую вершину при итерации"""
        if self._index < len(self._dfs_order):
            vertex = self._dfs_order[self._index]
            self._index += 1
            return vertex
        raise StopIteration

    def __str__(self):
        """Строковое представление"""
        result = []
        for vertex, neighbors in self.connections_list.items():
            result.append(f"{vertex}: {neighbors}")
        return "\n".join(result)

    def __contains__(self, vertex):
        """Проверка наличия вершины"""
        return vertex in self.connections_list

    # ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ ДЛЯ РАБОТЫ С ГРАФОМ

    def get_vertices(self):
        """Возвращает список всех вершин"""
        return list(self.connections_list.keys())

    def get_edges(self):
        """Возвращает список всех рёбер"""
        edges = set()
        for vertex, neighbors in self.connections_list.items():
            for neighbor in neighbors:
                edge = tuple(sorted((vertex, neighbor)))
                edges.add(edge)

        return list(edges)

    # ОСНОВНОЕ ЗАДАНИЕ

    def dfs(self, start_vertex=None):
        """
        Обход графа в глубину | Depth-first search | DFS
        """
        if not self.connections_list:
            return []

        # если none, берём 1-ую вершину из словаря
        if start_vertex is None:
            start_vertex = next(iter(self.connections_list))

        # проверяем существование начальной вершины
        if start_vertex not in self.connections_list:
            raise ValueError(f"Вершина {start_vertex} не существует в графе")

        visited = []  # посещённые вершины
        stack = [start_vertex]  # вершины, которые необходимо обработать

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                # добавляем в обратном порядке для сохранения естественного порядка
                for neighbor in reversed(self.connections_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited
