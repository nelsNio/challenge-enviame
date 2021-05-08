from django.shortcuts import render
from rest_framework import viewsets
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer

class EmpresaViewset(viewsets.ModelViewSet):
    queryset=Empresa.objects.all().order_by('-id')
    serializer_class=EmpresaSerializer