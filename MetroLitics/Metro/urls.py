from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('analiticas', views.analiticas , name='analiticas'),
    path('reportes',views.reportes, name='reportes')
]
