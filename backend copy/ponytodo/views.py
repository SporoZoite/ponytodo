from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PonytodoSerializer
from .models import Ponytodo

# Create your views here.

class PonytodoView(viewsets.ModelViewSet):
    serializer_class = PonytodoSerializer
    queryset = Ponytodo.objects.all()
