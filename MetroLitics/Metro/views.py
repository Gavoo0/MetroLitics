from django.shortcuts import render,redirect
from .models import Mantenedor_metro
from datetime import datetime, timedelta
# Create your views here.
def index(request):
    context={}
    return render(request,'Metro/index.html',context)

def analiticas(request):
    hoy = datetime.now().date()
    ayer = hoy - timedelta(days=1)
    lineas_ayer = Mantenedor_metro.objects.filter(fecha=ayer)
    lineas_hoy = Mantenedor_metro.objects.filter(fecha=hoy)
    context = {
        'hoy':hoy,
        'ayer':ayer,
        'lineas_ayer': lineas_ayer,
        'lineas_hoy': lineas_hoy
    }
    return render(request, 'Metro/analiticas.html',context)

def mantenedor_metro(request):
    context={}
    return render(request, 'Metro/mantenedor_metro.html',context)

def mantenedor_buses(request):
    context={}
    return render(request, 'Metro/mantenedor_buses.html',context)