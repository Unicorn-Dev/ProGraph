from .graph import Graph
from .pillowgraph import PillowGraph
from .exceptions import *


def AdjListDictToString(AdjListDict):
    """Convert AdjListDict to it's string representation"""
    assert isinstance(AdjListDict, dict)
    AdjListString = str(AdjListDict)
    return AdjListString

def StringToAdjListDict(AdjListString):
    """Convert AdjListString to it's dict representation"""
    assert isinstance(AdjListString, str)
    AdjListDict = eval(AdjListString, {'__builtins__':{}})
    assert isinstance(AdjListDict, dict)
    return AdjListDict

def get_graph_img(AdjList):
    G = PillowGraph(AdjList)
    return G.draw()

def add_vertex(graph, vertex):
    """
    Raise Exception if sometsing gone wrong
    and vertex is not added
    """
    assert isinstance(vertex, str)
    AdjListDict = StringToAdjListDict(graph.AdjList)
    if len(vertex) > 15:
        raise ToLongName(vertex)
    try:
        AdjListDict[vertex]
    except KeyError:
        pass
    else:
        raise VretexAlreadyExist(vertex)
    AdjListDict[vertex] = {}
    graph.AdjList = str(AdjListDict)
    graph.save()

def add_edge(graph, edge):
    """
    Raise Exception if sometsing gone wrong
    and edge is not added
    """
    assert isinstance(edge, str)
    AdjListDict = StringToAdjListDict(graph.AdjList)
    _to, _from, _weight = None, None, None
    try:
        _to, _from, _weight = edge.split()
    except:
        try:
            _to, _from = edge.split()
        except:    
            raise VretexNumberError(edge)
    else:
        try:
            _weight = int(_weight)
        except:
            raise IncorrectWeightError(edge)
    try:
        AdjListDict[_to]
        AdjListDict[_from]
    except KeyError:
        raise VretexDoesNotExist(edge)
    try:
        AdjListDict[_to][_from]
    except:
        AdjListDict[_to][_from] = []
    AdjListDict[_to][_from].append(_weight)
    graph.AdjList = str(AdjListDict)
    graph.save()

def delete_vertex(graph, vertex):
    """
    Raise Exception if sometsing gone wrong
    and vertex is not deleted
    """
    assert isinstance(vertex, str)
    AdjListDict = StringToAdjListDict(graph.AdjList)
    if len(vertex) > 15:
        raise ToLongName(vertex)
    try:
        AdjListDict[vertex]
    except KeyError:
        raise VretexDoesNotExist(vertex)
    del AdjListDict[vertex] 
    for edge_dic in AdjListDict.values():
        try:
            del edge_dic[vertex]
        except:
            pass
    graph.AdjList = str(AdjListDict)
    graph.save()

def delete_edge(graph, edge):
    """
    Raise Exception if sometsing gone wrong
    and edge is not deleted.
    """
    assert isinstance(edge, str)
    AdjListDict = StringToAdjListDict(graph.AdjList)
    _to, _from, _weight = None, None, None
    try:
        _to, _from, _weight = edge.split()
    except:
        try:
            _to, _from = edge.split()
        except:    
            raise VretexNumberError(edge)
    else:
        try:
            _weight = int(_weight)
        except:
            raise IncorrectWeightError(edge)
    try:
        AdjListDict[_to]
        AdjListDict[_from]
    except KeyError:
        raise VretexDoesNotExist(edge)
    try:
        AdjListDict[_to][_from]
        if _weight is None:
            AdjListDict[_to][_from].pop()
        else:
            AdjListDict[_to][_from].remove(_weight)
        if len(AdjListDict[_to][_from]) == 0:
            del AdjListDict[_to][_from]
    except:
        raise EdgeDoesNotExist(edge)
    graph.AdjList = str(AdjListDict)
    graph.save()