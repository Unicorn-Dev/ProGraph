from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'prographs/index.html')


def graph(request, graph_id):
    context = {'id': graph_id}
    return render(request, 'prographs/graph.html', context)
