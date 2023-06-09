from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from projects.models import usuario



def registro(request):
    return render(request, 'registro.html')

def inicio(request):
    return render(request, 'inicio.html')

def soporte(request):
    return render(request, 'soporte.html')

def iniciar(request):
    return render(request, 'iniciar.html')

def apostar(request):
    return render(request, 'apostar.html')

def apuestas(request):
    return render(request, 'apuestas.html')

def cambiar(request):
    return render(request, 'cambiar.html')

def configMediosP(request):
    return render(request, 'configMediosP.html')

def lista(request):
    return render(request, 'lista.html')

def opcionesA(request):
    return render(request, 'opcionesA.html')

def OpcionesU(request):
    return render(request, 'OpcionesU.html')
    

def recargar(request):
    return render(request, 'recargar.html')

def recuperar(request):
    return render(request, 'recuperar.html')

def retirar(request):
    return render(request, 'retirar.html')

def Ver_apuestas(request):
    return render(request, 'OpcionesU.html')


def usuario(request):
    if request.method == 'POST':
        nombres = request.POST['Nombres']
        apellidos = request.POST['Apellidos']
        ubicacion = request.POST['Ubicacion']
        direccion = request.POST['Dirección']
        tipo_doc = request.POST['Tipo_doc']
        n_doc = request.POST['N_doc']
        email = request.POST['Email']
        contraseña = request.POST['Contraseña']


        usuario = usuario(
        Nombres= nombres,
        Apellidos= apellidos,
        Ubicacion= ubicacion,
        Direccion= direccion,
        Tipo_doc= tipo_doc,
        N_doc= n_doc,
        Correo= email,
        Contraseña= contraseña,
        Fecha_Creacion=date.today()
        )

        usuario.save()

        return render(request, 'inicio.html')
    else:
        return render(request, 'registro.html')