from django.shortcuts import render, get_object_or_404

from .models import Restaurante, Platillo, Usuario
# Create your views here.

def index(request):

    lista_platillos = {}
    return render(request, 'bar/index.html', lista_platillos)

def details(request, platillo_id):
    platillo = get_object_or_404(Platillo, pk=platillo_id)
    return render(request, 'bar/detail.html', {'platillo': platillo})

def nosotros(request):
    return render(request, 'bar/nosotros.html',{})

def mapa(request):
    return render(request, 'bar/mapa.html', {})

def timeline(request):
    return render(request, 'bar/timeline.html', {})

def grafico(request):
    return render(request, 'bar/grafico.html', {})

def login(request):
    return render(request, 'bar/login.html', {})

def login_validation(request):
    usuario=request.POST.get('user_name')
    contrasenia=request.POST.get('user_password')
    login = True
    usuario_base = ""
    try:
    	usuario_base = Usuario.objects.get(pk=usuario)           
    except:
        login = False
    if (usuario != usuario_base):
        login = False
    if (login):
        request.session['usuario']=usuario
        request.session['contrasenia']=contrasenia
        return render(request, 'bar/login_validation.html', {'login':"login exitoso"})
    return render(request, 'bar/login_validation.html', {'login':"usuario incorrecto"})






