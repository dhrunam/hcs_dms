
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class ComplexList(generics.ListCreateAPIView):
    queryset = models.Complex.objects.all().order_by('id')
    serializer_class = serializers.ComplexSerializer


class ComplexDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Complex
    serializer_class = serializers.ComplexSerializer
