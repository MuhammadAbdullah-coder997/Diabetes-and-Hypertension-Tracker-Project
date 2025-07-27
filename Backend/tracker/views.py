from django.shortcuts import render
from rest_framework import viewsets
from .models import HealthMetric
from .serializers import HealthMetricSerializer

# Create your views here.

class HealthMetricViewSet(viewsets.ModelViewSet):
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricSerializer