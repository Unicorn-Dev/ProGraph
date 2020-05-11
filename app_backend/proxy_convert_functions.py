from .pillowgraph import PillowGraph
from graph.models import Graph
from django.utils import timezone


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
    gr = PillowGraph(StringToAdjListDict(graph.AdjList))
    gr.add_vertex(vertex)
    graph.AdjList = str(gr.AdjList)
    graph.save()

def add_edge(graph, edge):
    """
    Raise Exception if sometsing gone wrong
    and edge is not added
    """
    assert isinstance(edge, str)
    gr = PillowGraph(StringToAdjListDict(graph.AdjList))
    gr.add_edge(edge)
    graph.AdjList = str(gr.AdjList)
    graph.save()

def delete_vertex(graph, vertex):
    """
    Raise Exception if sometsing gone wrong
    and vertex is not deleted
    """
    assert isinstance(vertex, str)
    gr = PillowGraph(StringToAdjListDict(graph.AdjList))
    gr.delete_vertex(vertex)
    graph.AdjList = str(gr.AdjList)
    graph.save()

def delete_edge(graph, edge):
    """
    Raise Exception if sometsing gone wrong
    and edge is not deleted.
    """
    assert isinstance(edge, str)
    gr = PillowGraph(StringToAdjListDict(graph.AdjList))
    gr.delete_edge(edge)
    graph.AdjList = str(gr.AdjList)
    graph.save()

def create_graph():
    new_graph = Graph(AdjList={}, pub_date=timezone.now())
    new_graph.save()
    return new_graph.id
