from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Restaurante, Platillo, Precio
# Create your views here.

def index(request):

    lista_platillos = {}
    return render(request, 'mybarapp/index.html', lista_platillos)

def nosotros(request):
    return render(request, 'mybarapp/nosotros.html',{})

def mapa(request):
    return render(request, 'mybarapp/mapa.html', {})

def timeline(request):
    return render(request, 'mybarapp/timeline.html', {})

def grafico(request):
    return render(request, 'mybarapp/grafico.html', {})

class PlatilloListView(generic.ListView):
    model = Platillo

class PlatilloDetailView(generic.DetailView):
    model = Platillo