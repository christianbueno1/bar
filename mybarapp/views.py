from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

@login_required
def grafico(request):
    return render(request, 'mybarapp/grafico.html', {})

class PlatilloListView(LoginRequiredMixin,generic.ListView):
    model = Platillo

class PlatilloDetailView(LoginRequiredMixin, generic.DetailView):
    model = Platillo

class RestauranteListView(LoginRequiredMixin, generic.ListView):
    model = Restaurante

class RestauranteDetailView(LoginRequiredMixin,generic.DetailView):
    model = Restaurante

