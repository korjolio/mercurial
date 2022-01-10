from django.shortcuts import render, HttpResponse
from django.views.generic import *
from .models import Cliente

# Create your views here.

def index(request):
    return render(request, 'propuestas/index.html')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'propuestas/cliente/listado.html'