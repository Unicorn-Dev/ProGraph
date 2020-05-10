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
