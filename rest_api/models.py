from email.policy import default
from secrets import choice
from turtle import color
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

class Krosovka(models.Model):
    
    SPORT = 'SPORT'
    BAZM = 'BAZM'
    
    PRODUCT_FILTER = [
        (SPORT, 'Sport'),
        (BAZM, 'Bazm')
    ]
    
    brand = models.CharField(max_length=100)
    size = models.IntegerField(default=40)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=40)
    turi = models.CharField(max_length=10, choices=PRODUCT_FILTER, default=SPORT)
    

    def __str__(self):
        return f"{self.brand} nomli brand"