from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader
from .models import Producto
# Create your views here.

def DB_Productos(request):
    template = loader.get_template('productos.html')
    productos= Producto.objects.all().values()
    context={
        'productos_html': productos
    }

    return HttpResponse (template.render(context, request))