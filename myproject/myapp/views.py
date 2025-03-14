from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MySerializer
from .models import MyModel

class MyViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer