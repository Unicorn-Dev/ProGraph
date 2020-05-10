from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from app_backend import proxy_convert_functions as ps_funcs

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
    AdjList = ps_funcs.StringToAdjListDict(graph.AdjList)
    context =  {'graph': graph, 'graph_img': ps_funcs.get_graph_img(AdjList), 'error_message': error_message}
    return render(request, 'graph/concrete_graph.html', context)

def add_vertex(request, graph_id):
    graph = get_object_or_404(Graph, pk=graph_id)
    vertex = request.POST['vertex_name']
    vert_is_added = ps_funcs.add_vertex(graph, vertex)
    try:
    	pass
    except Exception as e:
        pass
    else:
        if vert_is_added:
            global error_message
            error_message = None
            return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
        else:
            error_message = 'This vertex already exist.'
            return HttpResponseRedirect(reverse('concrete_graph', args=(graph.id, )))
