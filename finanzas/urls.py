from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.landing, name='landing'),
    path('', views.dashboard, name='dashboard'),
    path('ingresos/', views.ingresos, name='ingresos'),
    path('gastos/', views.gastos, name='gastos'),
    path('categorias/', views.categorias, name='categorias'),
    path('informe/', views.informe, name='informe'),
    path('perfil/', views.perfil, name='perfil'),
]