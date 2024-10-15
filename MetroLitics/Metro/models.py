from django.db import models

# Create your models here.
class Mantenedor_metro(models.Model):
    id_metro = models.AutoField(primary_key=True)
    linea_metro = models.CharField(max_length=50)
    fecha = models.DateField()
    aglomeracion = models.IntegerField()
    
    def __str__(self):
        return self.linea_metro