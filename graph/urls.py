from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='graph_index'),
    path('<int:graph_id>/', views.concrete_graph, name='concrete_graph'),
    path('<int:graph_id>/add_vertex/', views.add_vertex, name='add_vertex'),
    path('<int:graph_id>/add_edge/', views.add_edge, name='add_edge'),
    path('<int:graph_id>/delete_vertex/', views.delete_vertex, name='delete_vertex'),
    path('<int:graph_id>/delete_edge/', views.delete_edge, name='delete_edge'),
    path('<int:graph_id>/dfs/complete', views.complete_dfs, name='complete_dfs'),
    path('<int:graph_id>/dfs/step/<int:algo_iteration>', views.next_step_dfs, name='next_step_dfs'),
    path('<int:graph_id>/bfs/complete', views.complete_bfs, name='complete_bfs'),
    path('<int:graph_id>/bfs/step/<int:algo_iteration>', views.next_step_bfs, name='next_step_bfs'),
]
