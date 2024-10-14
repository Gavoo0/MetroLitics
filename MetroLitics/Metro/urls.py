from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('analiticas', views.analiticas , name='analiticas'),
    path('mantenedor_metro',views.mantenedor_metro, name='mantenedor_metro'),
    path('mantenedor_buses',views.mantenedor_buses, name='mantenedor_buses')
]
