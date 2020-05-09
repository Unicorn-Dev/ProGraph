import networkx as nx


class Graph:
    def __init__(self, _vertices=[], _AdjMatrix = None):
        assert isinstance(_vertices, list)
        self.vertices = _vertices
        self.get_vertex_id = {v: i for i, v in enumerate(_vertices)}
        self.V = len(_vertices)
        self.E = 0
        self.AdjMatrix = [[[] for j in range(self.V)] for i in range(self.V)]
        self.nx = nx.MultiGraph().to_directed()

    def add_vertex(self, _vertex) -> None:
        self.vertices.append(_vertex)
        self.get_vertex_id[_vertex] = self.V
        self.V += 1
        if self.V == 1:
            self.AdjMatrix = [[[]]]
        else:
            for v in self.AdjMatrix:
                v.append([])
            self.AdjMatrix.append([[] * self.V])
        self.nx.add_node(_vertex)

    def add_edge(self, _from, _to, _weight=None) -> None:
        self.E += 1
        id_from, id_to = self.get_vertex_id[_from], self.get_vertex_id[_to]
        self.AdjMatrix[id_from][id_to].append(_weight)
        self.nx.add_edge(_from, _to)

    def is_edge_oriented(self, id_from, id_to) -> bool:
        return self.AdjMatrix[id_to][id_from] != []

    def draw(self, color='y'):
        import matplotlib.pyplot as plt
        from io import BytesIO
        from base64 import b64encode as encode


        x1, y1 = [-1, 12], [1, 4]
        x2, y2 = [1, 10], [3, 2]
        
        
        return '900'
