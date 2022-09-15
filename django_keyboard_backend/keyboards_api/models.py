from django.db import models

# Create your models here.

class Keyboard(models.Model):
    brand = models.CharField(max_length=24)
    switches = models.CharField(max_length=24)
    keycaps = models.CharField(max_length=24)
    stabilizers = models.CharField(max_length=24)
    price = models.IntegerField()
    size = models.CharField(max_length=24)