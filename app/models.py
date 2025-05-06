from django.db import models

class Catalogo(models.Model):
    ESTADO_CHOICES = [
        ('D', 'Disponible'),
        ('V', 'Vendido'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    edad = models.IntegerField()
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)

    class Meta:
        managed = False
        db_table = 'catalogos'




class Imagen(models.Model):
    catalogo = models.ForeignKey('Catalogo', on_delete=models.DO_NOTHING, related_name='imagenes')
    ruta = models.TextField()
    principal = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'imagenes'
