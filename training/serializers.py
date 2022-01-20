from dataclasses import fields
from rest_framework import serializers
from .models import Training

class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = [
            "pk",
            "name", 
            "distance", 
            "time",
            "date", 
        ]

