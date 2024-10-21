from django.shortcuts import render,redirect,get_object_or_404
from .models import Mantenedor_metro, Mantenedor_bus, Reporte
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def index(request):
    context={}
    return render(request,'Metro/index.html',context)

def analiticas(request):
    hoy = datetime.now().date()
    ayer = hoy - timedelta(days=1)


    buses_hoy = Mantenedor_bus.objects.filter(fecha__date=hoy)
    buses_ayer = Mantenedor_bus.objects.filter(fecha__date=ayer)


    buses_con_diferencias = []


    for bus_hoy in buses_hoy:
        

        aglomeracion_ayer = None
        cantidad_personas_ayer = None


        for bus_ayer in buses_ayer:
            if bus_ayer.f_id_metro.linea_metro == bus_hoy.f_id_metro.linea_metro:
                aglomeracion_ayer = bus_ayer.f_id_metro.aglomeracion
                cantidad_personas_ayer = bus_ayer.cantidad_personas
        

        diferencia_hoy = bus_hoy.f_id_metro.aglomeracion - bus_hoy.cantidad_personas

        if aglomeracion_ayer is not None and cantidad_personas_ayer is not None:
            diferencia_ayer = aglomeracion_ayer - cantidad_personas_ayer
        else:
            diferencia_ayer = None 


        buses_con_diferencias.append({
            'linea_metro': bus_hoy.f_id_metro.linea_metro,
            'diferencia_hoy': diferencia_hoy,
            'diferencia_ayer': diferencia_ayer,
        })

 
    context = {
        'buses_hoy':buses_hoy,
        'hoy': hoy,
        'ayer': ayer,
        'buses_con_diferencias': buses_con_diferencias,
    }


    return render(request, 'Metro/analiticas.html', context)




def reportes(request):
    if request.method == "POST":
        linea_metro = request.POST.get('linea')
        fecha_metro_str = request.POST.get('fecha') 
        aglomeracion = int(request.POST.get('aglomeracion'))
        fecha_bus_str = request.POST.get('fecha_bus') 
        personas_bus = int(request.POST.get('personas_bus'))
        fecha_metro_naive = datetime.strptime(fecha_metro_str, '%Y-%m-%dT%H:%M')

        fecha_metro = timezone.make_aware(fecha_metro_naive)

        fecha_bus_naive = datetime.strptime(fecha_bus_str, '%Y-%m-%dT%H:%M')
        fecha_bus = timezone.make_aware(fecha_bus_naive)

        metros = Mantenedor_metro.objects.filter(fecha__date=fecha_metro.date(), linea_metro=linea_metro)

        if metros.exists():
            metro = metros.first()
            metro.aglomeracion = (aglomeracion + metro.aglomeracion) - personas_bus
            metro.save()
        else:
            metro = Mantenedor_metro(
                linea_metro=linea_metro,
                fecha=fecha_metro,
                aglomeracion=aglomeracion
            )
            metro.save()

        buses = Mantenedor_bus.objects.filter(fecha__date=fecha_bus.date(), f_id_metro = metro)

        if buses.exists():
            bus = buses.first()
            bus.f_id_metro = metro
            bus.cantidad_personas = personas_bus
            bus.save()
        else:
            bus = Mantenedor_bus(
                f_id_metro=metro,
                fecha=fecha_bus,
                cantidad_personas=personas_bus
            )
            bus.save()

        nuevo_reporte = Reporte(
            f_id_metro=metro,
            f_id_bus=bus,
            fecha=fecha_metro
        )
        nuevo_reporte.save()
        messages.success(request, "El reporte ha sido creado correctamente")

    context = {}
    return render(request, 'Metro/reportes.html', context)

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
    total_personas = aglomeracion_metro - cantidad_personas_bus
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

def editar_reportes(request, id_reporte):
    reporte = get_object_or_404(Reporte, id_reporte=id_reporte)
    metro = reporte.f_id_metro
    bus = reporte.f_id_bus
    
    if request.method == "POST":
        # DATOS METRO
        aglomeracion = int(request.POST.get('aglomeracion'))
        
        #DATOS BUS
        cantidad_personas = int(request.POST.get('personas_bus'))
        
        metro.aglomeracion = aglomeracion
        bus.cantidad_personas = cantidad_personas
        metro.save()
        bus.save()
        messages.success(request, "Se ha actualizado correctamente.")
    context ={'metro':metro,
              'bus':bus,
              'reporte':reporte}
    return render(request,'Metro/editar_reportes.html',context)