from django.urls import path
from projects import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path('inicio/', views.inicio, name="inicio"),
    path('soporte/', views.soporte, name="soporte"),
    path('iniciar/', views.iniciar, name="iniciar"),
    path('apostar/', views.apostar, name="apostar"),
    path('apuestas/', views.apuestas, name="apuestas"),
    path('cambiar/', views.cambiar, name="cambiar"),
    path('configMedioP/', views.configMedioP, name="configMedioP"),
    path('lista/', views.lista, name="lista"),
    path('opcionesA/', views.opcionesA, name="opcionesA"),
    path('opcionesU/', views.opcionesU, name="opcionesU"),
    path('recargar/', views.recargar, name="recargar"),
    path('recuperar/', views.recuperar, name="recuperar"),
    path('resultado/', views.ressultado, name="resultado"),
    path('retirar/', views.retirar, name="retirar"),
    path('ver_apuesta/', views.ver_apuesta, name="ver_apuesta"),
]