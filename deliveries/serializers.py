from rest_framework import serializers
from deliveries.models import Delivery
# Register your models here.

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'