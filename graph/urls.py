from django.urls import path

from . import views

urlpatterns = [
    path('', views.graph_index, name='graph_index'),
    path('<int:graph_id>/', views.concrete_graph, name='concrete_graph'),
]

