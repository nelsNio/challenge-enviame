from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()

urlpatterns = [
    path('fibonacci/',views.fibonacci),
] + router.urls