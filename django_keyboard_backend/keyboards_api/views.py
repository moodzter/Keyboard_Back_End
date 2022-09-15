from django.shortcuts import render
from rest_framework import generics
from .serializers import KeyboardSerializer
from .models import Keyboard
# Create your views here.

class KeyboardList(generics.ListCreateAPIView):
    queryset = Keyboard.objects.all().order_by('id')
    serializer_class = KeyboardSerializer 

class KeyboardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyboard.objects.all().order_by('id')
    serializer_class = KeyboardSerializer 