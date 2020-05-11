from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from app_backend import proxy_convert_functions as pc_funcs
from app_backend.exceptions import *
from .models import Graph


class IndexView(generic.ListView):
    template_name = 'graph/index.html'
    context_object_name = 'latest_graph_list'

    def get_queryset(self):
        """Return the last five published graphs."""
        return Graph.objects.order_by('-pub_date')[:5]


class ConcreteView(generic.DetailView):
    model = Graph
    template_name = 'graph/concrete_graph.html'

error_message = None
def concrete_graph(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    AdjList = pc_funcs.StringToAdjListDict(graph.AdjList)
    global error_message
    context =  {
                    'graph': graph,
                    'graph_img': pc_funcs.get_graph_img(AdjList),
                    'error_message': error_message
                }
    error_message = None
    return render(request, 'graph/concrete_graph.html', context)

def add_vertex(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['vertex_name']
    global error_message
    try:
    	pc_funcs.add_vertex(graph, vertex)
    except ToLongName:
        error_message = 'Vertex name is too long.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    except VretexAlreadyExist:
        error_message = 'This vertex already exist.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    error_message = None
    return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))

def add_edge(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    edge = request.POST['edge_name']
    global error_message
    try:
    	pc_funcs.add_edge(graph, edge)
    except IncorrectWeightError:
        error_message = 'Weight should be integer.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    except VretexNumberError:
        error_message = 'Expected 2 vertex.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    except VretexDoesNotExist:
        error_message = 'One of vertex isn\'t exist.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    error_message = None
    return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))

def delete_vertex(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['vertex_name']
    global error_message
    try:
    	pc_funcs.delete_vertex(graph, vertex)
    except VretexDoesNotExist:
        error_message = 'Vertex isn\'t exist.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    error_message = None
    return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))

def delete_edge(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    edge = request.POST['edge_name']
    global error_message
    try:
    	pc_funcs.delete_edge(graph, edge)
    except IncorrectWeightError:
        error_message = 'Weight should be integer.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    except VretexNumberError:
        error_message = 'Expected 2 vertex.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    except EdgeDoesNotExist:
        error_message = 'Edge isn\'t exist.'
        return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
    error_message = None
    return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))