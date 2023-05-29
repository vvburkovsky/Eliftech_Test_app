from typing import Any
from django.db import models

# Create your models here.


class Restorans(models.Model):
    RestoranName = models.CharField(max_length=128)
    
    def __str__ (self):
        return(self.RestoranName)
    
class Restorans_menu(models.Model):
    MCDONALDS = 'McDonalds'
    KFC = 'Kfc'
    PAPAJOE = 'PapaJoe'
    ETC = 'etc'

    CHOSE_GROUP = {
        (MCDONALDS, 'McDonalds'),
        (KFC, 'Kfc'),
        (PAPAJOE, 'PapaJoe'),
        (ETC, 'etc'),
    }

    name = models.CharField(max_length=100)
    #name = models.ForeignKey(Restorans, on_delete=models.CASCADE)    
    description = models.CharField(max_length=128)
    img = models.ImageField()
    price = models.IntegerField()
    group = models.CharField(max_length=20, choices=CHOSE_GROUP, default=MCDONALDS)

    def __str__(self):
        return(self.description)
    

class Basket(models.Model):
    order_name = models.CharField(max_length=100)
    img = models.ImageField()
    price = models.IntegerField()

    def __str__(self):
        return(self.order_name)