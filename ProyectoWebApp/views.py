from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

def home(request):

    return render(request, 'ProyectoWebApp/home.html')


def tienda(request):

    return render(request, 'ProyectoWebApp/tienda.html')

def blog(request):

    return render(request, 'ProyectoWebApp/blog.html')

def contacto(request):

    return render(request, 'ProyectoWebApp/contacto.html')
