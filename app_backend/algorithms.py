from .pillowgraph import PillowGraph
from graph.models import Graph
from app_backend import proxy_convert_functions as pc_funcs
from queue import Queue


def dfs(graph, vertex):
    assert isinstance(vertex, str)
    gr = PillowGraph(pc_funcs.StringToAdjListDict(graph.AdjList))
    graph.AlgoSequense = ''
    colors = {vertex: 'W' for vertex in gr.vertices}
    sequence = []
    gr.dfs(vertex, colors, sequence)
    sequence = 'dfs', vertex, sequence
    graph.AlgoSequense = str(sequence)
    graph.save()


def bfs(graph, vertex):
    assert isinstance(vertex, str)
    gr = PillowGraph(pc_funcs.StringToAdjListDict(graph.AdjList))
    graph.AlgoSequense = ''
    walked = {vertex: False for vertex in gr.vertices}
    walked[vertex] = True
    queue = Queue()
    queue.put(vertex)
    sequence = []
    gr.bfs(queue, walked, sequence)
    sequence = 'bfs', vertex, sequence
    graph.AlgoSequense = str(sequence)
    graph.save()
