from .graph import Graph
from .pillowgraph import PillowGraph


def AdjListDictToString(AdjListDict):
    """Convert AdjListDict to it's string representation"""
    assert isinstance(AdjListDict, dict)
    AdjListString = str(AdjListDict)
    return AdjListString

def StringToAdjListDict(AdjListString):
    """Convert AdjListString to it's dict representation"""
    assert isinstance(AdjListString, str)
    AdjListDict = eval(AdjListString)
    assert isinstance(AdjListDict, dict)
    return AdjListDict

def get_graph_img(AdjList):
    G = PillowGraph(AdjList)
    return G.draw()

def add_vertex(graph, vertex):
    """Return False if vertex already exist"""
    AdjListDict = StringToAdjListDict(graph.AdjList)
    try:
        vertex = int(vertex)
    except Exception as e:
        pass
    try:
        AdjListDict[vertex]
    except Exception as e:
        pass
    else:
        return False
    AdjListDict[vertex] = {}
    graph.AdjList = str(AdjListDict)
    graph.save()
    return True
