from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    context={}
    return render(request,'Metro/index.html',context)

def iniciar_sesion(request):
    context={}
    return render(request,'Metro/iniciar_sesion.html',context)

def analiticas(request):
    context={}
    return render(request, 'Metro/analiticas.html',context)