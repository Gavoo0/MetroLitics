from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    context={}
    return render(request,'Metro/index.html',context)