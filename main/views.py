from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app_backend import proxy_convert_functions as pc_funcs


def index(request):
    """The home page for Pro Graph"""
    return render(request, 'main/index.html')

def get_graph(request):
    """The home page for Pro Graph"""
    graph_id = request.POST['graph_id']
    return HttpResponseRedirect(reverse('graph:concrete_graph', args=(graph_id, )))

def new_graph(request):
    """The home page for Pro Graph"""
    graph_id = pc_funcs.create_graph()
    return HttpResponseRedirect(reverse('graph:concrete_graph', args=(graph_id, )))
