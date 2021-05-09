from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from deliveries.models import Delivery
from deliveries.api import Enviame
from deliveries.serializers import DeliverySerializer



"""
Vista encargada de CRUD basica para la entidad Delivery
POST:       http://0.0.0.0:8000/api/v1/deliveries/  JSON
GET:        http://0.0.0.0:8000/api/v1/deliveries/ 
PATCH:      http://0.0.0.0:8000/api/v1/deliveries/{id}/ JSON
DELETE:     http://0.0.0.0:8000/api/v1/deliveries/{id}/

"""
class DeliveryViewset(viewsets.ModelViewSet):
    queryset=Delivery.objects.all().order_by('-id')
    serializer_class=DeliverySerializer



    def create(self,request):
        enviame= Enviame()
        delivery_api=enviame.post(request.data)
        deliveries=delivery_api.json()['data']
        for delivery in deliveries:
            serializer= DeliverySerializer(data=delivery)
            if serializer.is_valid(raise_exception=True):
                Delivery(**serializer.validated_data).save()
        return Response({'ok':True,'delivery' :delivery_api.json()['data']})





    @action(methods=['GET'], detail=False)
    def estimate_delivery_time(self):

        pass