"""Определяет схемы URL для prographs"""

from django.urls import path
from . import views

app_name = 'graph'
urlpatterns = [
    path('<int:graph_id>', views.graph, name='graph'),
]
