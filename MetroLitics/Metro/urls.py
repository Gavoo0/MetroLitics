from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('analiticas', views.analiticas , name='analiticas'),
    path('reportes',views.reportes, name='reportes'),
    path('ver_reportes',views.ver_reportes, name='ver_reportes'),
    path('mostrar_reporte/<int:id_reporte>/',views.mostrar_reporte,name='mostrar_reporte'),
    path('editar_reportes/<int:id_reporte>/',views.editar_reportes,name='editar_reportes')
]
