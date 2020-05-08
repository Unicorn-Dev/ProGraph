from django.shortcuts import render
from graph.Graphs import Graph


def graph(request, graph_id):
    G = Graph([1, 2, 'Moscow', 'Peter', 5, 6, 7, 8])
    G.add_edge(1, 2)
    G.add_edge(1, 2)
    G.add_edge(2, 1)
    context = {'id': graph_id, 'graph': G.draw()}
    return render(request, 'graph/graph.html', context)
