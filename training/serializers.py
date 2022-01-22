from dataclasses import fields
from rest_framework import serializers
from .models import Training

class TrainingSerializers(serializers.ModelSerializer):       # serializers of Trening Models 
    class Meta:
        model = Training
        fields = [
            "pk",
            "name", 
            "distance", 
            "time",
            "date", 
        ]
