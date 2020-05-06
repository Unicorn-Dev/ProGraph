class Vertex:
    def __init__(self, _id, _x, _y, _text) -> None:
        self.x = _x
        self.y = _y
        self.text = _text

    def coordinates(self) -> tuple:
        return self.x, self.y

    def change_coordinates(self, _x, _y) -> None:
        self.x = _x
        self.y = _y

    def change_text(self, _text) -> None:
        self.text = _text

    def draw(self) -> None:
        pass


class Edge:
    def __init__(self, _weight=None) -> None:
        self.weight = _weight

    def change_weight(self, _weight):
        self.weight = _weight

    def draw(self, _from, _to, number_of_same_edges=0):
        pass


class Graph:
    def __init__(self, _vertices=[]):
        self.vertices = _vertices
        self.get_vertex = {i: v for i, v in enumerate(_vertices)}
        self.V = len(_vertices)
        self.E = 0
        self.AdjMatrix = [[[] * self.V] * self.V]

    def add_vertex(self, _vertex) -> None:
        self.vertices.append(_vertex)
        self.get_vertex[self.V] = _vertex
        self.V += 1
        if self.V == 1:
            self.AdjMatrix = [[[]]]
        else:
            for v in self.AdjMatrix:
                v.append([])
            self.AdjMatrix.append([[] * self.V])

    def add_edge(self, id_from, id_to, _weight) -> None:
        self.E += 1
        edge = Edge(_weight)
        self.AdjMatrix[id_from][id_to].append(edge)

    def is_edge_oriented(self, id_from, id_to) -> bool:
        return self.AdjMatrix[id_to][id_from] != []

    def draw(self) -> None:
        for v in self.vertices:
            v.draw()
        for i, from_list in enumerate(self.AdjMatrix):
            _from = self.get_vertex[i]
            for j, to_list in enumerate(from_list):
                _to = self.get_vertex[j]
                num_of_same_edges = len(to_list) - 1
                for edge in to_list:
                    edge.draw(_from, _to, num_of_same_edges)
