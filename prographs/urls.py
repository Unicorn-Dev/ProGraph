"""Определяет схемы URL для prographs"""

from django.urls import path
from . import views

app_name = 'prographs'
urlpatterns = [
    path('', views.index, name='index'),
    path('graph/<int:graph_id>', views.graph, name='graph'),
]
