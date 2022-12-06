from django.shortcuts import render
from django.http import HttpResponse
from MVT18Daneri.models import Familia
from django.core import serializers
import datetime
# Create your views here.
def familiar(request):
    famili=Familia(edad=20,nombre="Nick Dan", fecha="2022-08-20")
    famili.save()
    cadena=f"Familiar Agregado: Nombre{famili.nombre}, Edad: {famili.edad}, Fecha: {famili.fecha}"
    return HttpResponse(cadena)

def listar_familia(request):
    data= serializers.serialize("python",Familia.objects.all())
    context = {'data' : data, }

    return render(request, "MVT18Daneri/ListaFamiliar.html",context)

def inicio(request):
    return render(request, "MVT18Daneri/index.html")
