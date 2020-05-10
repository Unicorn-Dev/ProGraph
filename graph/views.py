from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Graph
from app_backend import proxy_convert_functions as ps_funcs


def graph_index(request):
    latest_graph_list = Graph.objects.order_by('-pub_date')[:5]
    context = {'latest_graph_list': latest_graph_list}
    return render(request, 'graph/index.html', context)

def concrete_graph(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    AdjList = ps_funcs.StringToAdjListDict(graph.AdjList)
    context =  {'graph': graph, 'graph_img': ps_funcs.get_graph_img(AdjList)}
    return render(request, 'graph/concrete_graph.html', context)

