from django.urls import path
from . import views


app_name = 'mybarapp'
urlpatterns = [
    path('',views.index, name='index'),
    # path('<int:platillo_id>/', views.details, name='detail'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('mapa/', views.mapa, name='mapa'),
    path('timeline/', views.timeline, name='timeline'),
    path('grafico/', views.grafico, name='grafico'),
    path('platillos/', views.PlatilloListView.as_view(), name='platillos'),
    path('platillo/<int:pk>', views.PlatilloDetailView.as_view(), name='platillo-detail'),
    path('restaurantes/', views.RestauranteListView.as_view(), name='restaurantes'),
    path('restaurante/<int:pk>', views.RestauranteDetailView.as_view(), name='restaurante-detail'),
]