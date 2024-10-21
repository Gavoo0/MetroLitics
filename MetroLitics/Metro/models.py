from django.db import models
from datetime import datetime
# Create your models here.
class Mantenedor_metro(models.Model):
    id_metro = models.AutoField(primary_key=True)
    linea_metro = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    aglomeracion = models.IntegerField()
    
    def __str__(self):
        return self.linea_metro + " (" + self.fecha.strftime('%Y-%m-%d') + ")"

class Mantenedor_bus(models.Model):
    id_bus = models.AutoField(primary_key=True)
    f_id_metro = models.ForeignKey(Mantenedor_metro,on_delete=models.CASCADE,db_column='id_metro')
    fecha = models.DateTimeField(null=True)
    cantidad_personas = models.IntegerField()
    
    def __str__(self):
        return self.f_id_metro.linea_metro + " (" + self.fecha.strftime('%Y-%m-%d') + ")"


class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    f_id_metro = models.ForeignKey(Mantenedor_metro,on_delete=models.CASCADE,db_column='id_metro')
    f_id_bus = models.ForeignKey(Mantenedor_bus,on_delete=models.CASCADE,db_column='id_bus',null=True)
    fecha = models.DateTimeField()
    
    def __str__(self):
        return self.f_id_metro.linea_metro+ " (" + self.fecha.strftime('%Y-%m-%d') + ")"