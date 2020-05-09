from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """The home page for Pro Graph"""
    return render(request, 'main/index.html')
