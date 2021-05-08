from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register('empresas', views.EmpresaViewset )

urlpatterns = router.urls