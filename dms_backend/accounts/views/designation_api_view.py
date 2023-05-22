
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class DesignationList(generics.ListCreateAPIView):
    queryset = models.Designation.objects.all().order_by('id')
    serializer_class = serializers.DesignationSerializer


class DesignationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Designation
    serializer_class = serializers.DesignationSerializer
