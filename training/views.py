from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
import training 
from .models import Training
from .serializers import TrainingSerializers
from django.db.models import Max, Avg
from training import serializers



class TrainingList(generics.ListCreateAPIView):  # list view of all tranings and methods PUT and GET 
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers

class TrainingDetail(generics.RetrieveUpdateDestroyAPIView):  # views of Trening Details and methods GET PUT DELETE 
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers



@api_view(['GET'])       # endpoint view of the lognest distance traveled  
def statistics(request):
    
    if request.method == 'GET':
        maximum = Training.objects.aggregate(m=Max('distance')).get('m')  # function returns the lognest distance traveled 
        time = Training.objects.all().aggregate(z=Avg('time')).get('z')  # function returns the average training time 
        time_round = round(time,2)
        return Response({"distancemax": maximum ,"avg_time":time_round})  # making the JSON from get data 






    
