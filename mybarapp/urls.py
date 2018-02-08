from django.urls import path

from . import views

app_name = 'bar'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:platillo_id>/', views.details, name='detail'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('mapa/', views.mapa, name='mapa'),
    path('timeline/', views.timeline, name='timeline'),
    path('grafico/', views.grafico, name='grafico'),
]