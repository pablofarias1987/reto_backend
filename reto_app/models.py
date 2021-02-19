from django.db import models

# Create your models here.
class Credito(models.Model):
    codigo = models.IntegerField()
    deuda = models.IntegerField()
    monto = models.IntegerField()
    cliente = models.CharField(max_length=30)
    puntaje =models.IntegerField()

