from rest_framework import serializers
from empresa.models import Empresa
# Register your models here.
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'