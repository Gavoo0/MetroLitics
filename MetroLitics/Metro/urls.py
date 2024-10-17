from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('analiticas', views.analiticas , name='analiticas'),
    path('reportes',views.reportes, name='reportes'),
    path('ver_reportes',views.ver_reportes, name='ver_reportes')
]
