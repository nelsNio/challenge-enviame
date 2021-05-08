from django.db import models

# Create your models here.

class Empresa(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    

    def __str__(self):
        return self.address + ' ' +self.name

    def __unicode__(self):
        return 

