from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer
from faker import Faker



class EmpresaViewset(viewsets.ModelViewSet):
    queryset=Empresa.objects.all().order_by('-id')
    serializer_class=EmpresaSerializer


    @action(methods=['POST'],detail=False)
    def fill_data(self, pk=None):
        print('fill_data in entity empresa')
        fake = Faker()
        for _ in range(10):
            name=fake.name()
            address=fake.address()
            print(name,"  ", address)
            serializer= EmpresaSerializer(data={'name':name,'address':address})
            if serializer.is_valid(raise_exception=True):
                Empresa(**serializer.validated_data).save()


        return Response({'ok':True}) 
