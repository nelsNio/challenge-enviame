from django.db import models

# Create your models here.
"""
Modelo de la entidad Empresa
"""
class Empresa(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    

    def __str__(self):
        return self.address + ' ' +self.name

    def __unicode__(self):
        return 

