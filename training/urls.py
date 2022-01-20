from django.urls import path
from . import views

urlpatterns = [
    path("training/", views.TrainingList.as_view()),
    path("training/<int:pk>", views.TrainingDetail.as_view())
   
]