from django.db import models


class Apostas_1(models.Model):
    numeros = models.CharField(max_length=255)
    
