from django.db import models

# Create your models here.

class Familia(models.Model):
    edad= models.IntegerField()
    nombre = models.CharField(max_length=50)
    fecha=models.DateField(format("DD/MM/YYYY"))