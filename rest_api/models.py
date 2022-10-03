from email.policy import default
from turtle import color
from django.db import models
from django.forms import IntegerField

class Krosovka(models.Model):
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=40)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=40)

    def __str__(self):
        return f"{self.brand} brandi"