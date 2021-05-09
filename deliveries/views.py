from django.http import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from deliveries.models import Delivery
from deliveries.api import Enviame
from deliveries.serializers import DeliverySerializer
from random import randint



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



    """
    Ejercicio 4: Consumo API Envíame para la creación de un envío
    Metodo recibir informacion, cunsumir API y guardar respuesta en la DB
    """
    def create(self,request):
        enviame= Enviame()
        delivery_api=enviame.post(request.data)
        deliveries=delivery_api.json()['data']
        for delivery in deliveries:
            serializer= DeliverySerializer(data=delivery)
            if serializer.is_valid(raise_exception=True):
                Delivery(**serializer.validated_data).save()
        return Response({'ok':True,'delivery' :delivery_api.json()['data']})




    """
    Ejercicio 6: Análisis + Desarrollo Aplicado a Negocio
    Metodo para calcular dias de entrega segun distancia y rango de diatancias
    """
    @action(methods=['GET'], detail=False)
    def estimate_delivery_time(self,request):
        ranges = [{'range': x + 1, 'distance': ((x + 1) * 100), 'days': x} for x in
          range(20)]  # TABLA DE RANGOS Y PARAMETROS DE ENVIO

        num = randint(0, 2000)
        print('Distancia a enviar', num)

        days = None
        current = None
        for x in range(len(ranges) - 1):
            current = ranges[x - 1]
            if num < current['distance'] and days is not None:
                days = current
                break

            if num < current['distance']:
                days = current
        if days['range'] == 2 or days['range'] == 3:
            days['days'] = 1
        elif days['range'] == 1 :
            days['days'] = 0
        else:
            days['days'] = days['days'] - 1

        return Response({'ok':True,'msg':f"Para una distancia de {num} Km(s), tu pedido llega en {days['days']} dia(s)."})