from django.shortcuts import render,redirect
from .models import Metro

# Create your views here.
def index(request):
    context={}
    return render(request,'Metro/index.html',context)

def analiticas(request):
    context={}
    return render(request, 'Metro/analiticas.html',context)

def mantenedor_metro(request):
    context={}
    return render(request, 'Metro/mantenedor_metro.html',context)

def mantenedor_buses(request):
    context={}
    return render(request, 'Metro/mantenedor_buses.html',context)