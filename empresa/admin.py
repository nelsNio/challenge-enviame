from django.contrib import admin
from empresa.models import Empresa
# Register your models here.
@admin.register(Empresa)
class AdminEmpresa(admin.ModelAdmin):
    list_display=[field.name for field in Empresa._meta.get_fields()]


