from turtle import distance
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.gis.measure import D, Distance

class Training(models.Model):              
    name = models.CharField(max_length=255)
    distance = models.FloatField(default=0)
    time = models.TimeField(default=0)
    date = models.DateField(default=0)


    def __str__(self):
        return self.title 


    