from django.shortcuts import render


# Create your views here.
def graph(request, graph_id):
    context = {'id': graph_id}
    return render(request, 'graph/graph.html', context)
