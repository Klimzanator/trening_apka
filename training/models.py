from datetime import datetime
from django.db import models
from django.forms import forms, widgets

class Training(models.Model):              # model of traingn objects  
    name = models.CharField(max_length=255)
    distance = models.FloatField(blank = False) # by default it is given in kilometers 
    time = models.FloatField(blank = False) # by default in minutes
    date = models.DateField(blank=False)


    def __str__(self):
        return self.title 


    