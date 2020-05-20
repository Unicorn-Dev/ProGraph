from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from app_backend import proxy_convert_functions as pc_funcs
import app_backend.algorithms as alg
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


def concrete_graph(request, graph_id=0):
    graph = get_object_or_404(Graph, pk=graph_id)
    AdjList = pc_funcs.StringToAdjListDict(graph.AdjList)
    graph.AlgoSequense = ''

    global error_message

    context = {
        'graph': graph,
        'graph_img': pc_funcs.get_graph_img(AdjList),
        'error_message': error_message,
        'algo': None,
        'algo_iteration': 0,
        'method': request.method,
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
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    except VretexAlreadyExist:
        error_message = 'This vertex already exist.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))


def add_edge(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    edge = request.POST['edge_name']
    global error_message
    try:
        pc_funcs.add_edge(graph, edge)
    except IncorrectWeightError:
        error_message = 'Weight should be integer.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    except VretexNumberError:
        error_message = 'Expected 2 vertex.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    except VretexDoesNotExist:
        error_message = 'One of vertex isn\'t exist.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))


def delete_vertex(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['vertex_name']
    global error_message
    try:
        pc_funcs.delete_vertex(graph, vertex)
    except VretexDoesNotExist:
        error_message = 'Vertex isn\'t exist.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))


def delete_edge(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    edge = request.POST['edge_name']
    global error_message
    try:
        pc_funcs.delete_edge(graph, edge)
    except IncorrectWeightError:
        error_message = 'Weight should be integer.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    except VretexNumberError:
        error_message = 'Expected 2 vertex.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    except EdgeDoesNotExist:
        error_message = 'Edge isn\'t exist.'
        return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))


# Algorithms

def complete_dfs(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['start_vertex']
    global error_message

    try:
        alg.dfs(graph, vertex)
    except:
        error_message = 'DFS failed.'
        return HttpResponseRedirect(
            reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:next_step_dfs', kwargs={
        'graph_id': graph.id,
        'algo_iteration': 0,
    }))


def next_step_dfs(request, graph_id, algo_iteration):
    graph = get_object_or_404(Graph, pk=graph_id)
    AdjList = pc_funcs.StringToAdjListDict(graph.AdjList)
    algo, start, AlgoSequense = pc_funcs.StringToAlgoSequenseList(graph.AlgoSequense)
    if algo != 'dfs':
        return HttpResponseRedirect(
            reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    algo_iteration += 1
    if not AlgoSequense and algo_iteration > 1:
        return HttpResponseRedirect(reverse('graph:next_step_dfs', kwargs={
            'graph_id': graph.id,
            'algo_iteration': 0,
        }))
    elif algo_iteration > len(AlgoSequense) and AlgoSequense:
        return HttpResponseRedirect(reverse('next_step_dfs', kwargs={
            'graph_id': graph.id,
            'algo_iteration': len(AlgoSequense) - 1,
        }))

    global error_message

    context = {
        'graph': graph,
        'graph_img': pc_funcs.get_graph_img_with_algo(AdjList, AlgoSequense, algo_iteration),
        'error_message': error_message,
        'algo': 'dfs',
        'algo_iteration': algo_iteration,
        'method': request.method,
        'algo_finished': algo_iteration >= len(AlgoSequense),
        'start_vertex': start,
    }
    error_message = None
    return render(request, 'graph/concrete_graph.html', context)


def complete_bfs(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['start_vertex']
    global error_message

    try:
        alg.bfs(graph, vertex)
    except:
        error_message = 'BFS failed.'
        return HttpResponseRedirect(
            reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    error_message = None
    return HttpResponseRedirect(reverse('graph:next_step_bfs', kwargs={
        'graph_id': graph.id,
        'algo_iteration': 0,
    }))


def next_step_bfs(request, graph_id, algo_iteration):
    graph = get_object_or_404(Graph, pk=graph_id)
    AdjList = pc_funcs.StringToAdjListDict(graph.AdjList)
    algo, start, AlgoSequense = pc_funcs.StringToAlgoSequenseList(graph.AlgoSequense)
    if algo != 'bfs':
        return HttpResponseRedirect(
            reverse('graph:concrete_graph', kwargs={'graph_id': graph.id}))
    algo_iteration += 1
    if not AlgoSequense and algo_iteration > 1:
        return HttpResponseRedirect(reverse('graph:next_step_bfs', kwargs={
            'graph_id': graph.id,
            'algo_iteration': 0,
        }))
    elif algo_iteration > len(AlgoSequense) and AlgoSequense:
        return HttpResponseRedirect(reverse('graph:next_step_bfs', kwargs={
            'graph_id': graph.id,
            'algo_iteration': len(AlgoSequense) - 1,
        }))

    global error_message

    context = {
        'graph': graph,
        'graph_img': pc_funcs.get_graph_img_with_algo(AdjList, AlgoSequense, algo_iteration),
        'error_message': error_message,
        'algo': 'bfs',
        'algo_iteration': algo_iteration,
        'method': request.method,
        'algo_finished': algo_iteration >= len(AlgoSequense),
        'start_vertex': start,
    }
    error_message = None
    return render(request, 'graph/concrete_graph.html', context)
