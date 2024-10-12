from django.db import models

# Create your models here.
class Metro(models.Model):
    id_metro = models.AutoField(primary_key=True)
    estacion = models.CharField(max_length=50)
    linea_metro = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now=True)
    cantidad_aglomeracion = models.IntegerField(default=1000)
    
    def __str__(self):
        return self.estacion