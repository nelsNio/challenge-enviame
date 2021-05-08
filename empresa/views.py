from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer
from faker import Faker


"""
Vista encargada de CRUD basica para la entidad empresa
POST:       http://0.0.0.0:8000/api/v1/fibonacci/  JSON
GET:        http://0.0.0.0:8000/api/v1/fibonacci/ 
PATCH:      http://0.0.0.0:8000/api/v1/fibonacci/{id}/ JSON
DELETE:     http://0.0.0.0:8000/api/v1/fibonacci/{id}/

"""
class EmpresaViewset(viewsets.ModelViewSet):
    queryset=Empresa.objects.all().order_by('-id')
    serializer_class=EmpresaSerializer


    """
    Inserta empresas con ayuda de la libreria Faker
    POST:   http://0.0.0.0:8000/api/v1/empresas/fill_data/
    """
    @action(methods=['POST'],detail=False)
    def fill_data(self, pk=None):
        print('fill_data in entity empresa')
        fake = Faker()
        for _ in range(10):
            name=fake.name()
            address=fake.address()
            serializer= EmpresaSerializer(data={'name':name,'address':address})
            if serializer.is_valid(raise_exception=True):
                Empresa(**serializer.validated_data).save()
        return Response({'ok':True})