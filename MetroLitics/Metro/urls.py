from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('iniciar_sesion',views.iniciar_sesion,name="iniciar_sesion"),
    path('analiticas', views.analiticas , name='analiticas')
]
