from django.shortcuts import render,redirect
from .models import Mantenedor_metro, Mantenedor_bus, Reporte
from datetime import datetime, timedelta
from django.core.paginator import Paginator
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

def reportes(request):
    if request.method == "POST":
        linea_metro = request.POST.get('linea')
        fecha_metro = request.POST.get('fecha')
        aglomeracion = int(request.POST.get('aglomeracion'))
        fecha_bus = request.POST.get('fecha_bus')
        personas_bus = int(request.POST.get('personas_bus'))
        

        metros = Mantenedor_metro.objects.filter(fecha=fecha_metro, linea_metro=linea_metro)

        if metros.exists():
            # Si ya existen registros, actualizamos el primero
            metro = metros.first()
            metro.aglomeracion = (aglomeracion + metro.aglomeracion)-personas_bus
            metro.save()
        else:
            # Si no existe, creamos un nuevo registro
            print("hola")
            metro = Mantenedor_metro(
                linea_metro=linea_metro,
                fecha=fecha_metro,
                aglomeracion=aglomeracion-personas_bus
            )
            metro.save()
        
        bus = Mantenedor_bus.objects.filter(fecha=fecha_bus)

        buses = Mantenedor_bus.objects.filter(fecha=fecha_bus)

        if buses.exists():
            # Si ya existen registros, actualizamos el primero
            bus = buses.first()
            bus.f_id_metro = metro
            bus.cantidad_personas = personas_bus
            bus.save()
        else:
            # Si no existe, lo creamos
            bus = Mantenedor_bus(
                f_id_metro=metro,
                fecha=fecha_bus,
                cantidad_personas=personas_bus
            )
            bus.save()
        
        nuevo_reporte = Reporte(
            f_id_metro = metro,
            f_id_bus = bus,
            fecha = fecha_metro
        )
        
        nuevo_reporte.save()
        
    context={}
    return render(request, 'Metro/reportes.html',context)

def ver_reportes(request):
    reportes_list = Reporte.objects.all()
    paginator = Paginator(reportes_list, 5)  # Mostramos 10 reportes por página

    # Obtener el número de página desde la solicitud GET
    page_number = request.GET.get('page')
    reportes = paginator.get_page(page_number)

    context = {'reportes': reportes}
    return render(request, 'Metro/ver_reportes.html', context)


def mostrar_reporte(request,id_reporte):
    reporte = Reporte.objects.get(pk=id_reporte)
    linea_metro = reporte.f_id_metro.linea_metro
    aglomeracion_metro = reporte.f_id_metro.aglomeracion
    cantidad_personas_bus = reporte.f_id_bus.cantidad_personas
    total_personas = aglomeracion_metro + cantidad_personas_bus
    fecha = reporte.fecha

    # Crear el contexto para pasar los datos a la plantilla
    context = {
        'linea_metro': linea_metro,
        'aglomeracion_metro': aglomeracion_metro,
        'cantidad_personas_bus': cantidad_personas_bus,
        'total_personas': total_personas,
        'fecha': fecha
    }
    return render(request, 'Metro/mostrar_reporte.html',context)