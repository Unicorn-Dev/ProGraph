from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_graph/', views.get_graph, name='get_graph'),
    path('new_graph/', views.new_graph, name='new_graph'),
]
