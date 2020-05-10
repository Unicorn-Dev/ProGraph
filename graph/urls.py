from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='graph_index'),
    path('<int:graph_id>/', views.concrete_graph, name='concrete_graph'),
    path('<int:graph_id>/add_vertex', views.add_vertex, name='add_vertex'),
]

