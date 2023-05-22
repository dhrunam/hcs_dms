
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class DesignationAllocationList(generics.ListCreateAPIView):
    queryset = models.DesignationAllocation.objects.all().order_by('id')
    serializer_class = serializers.DesignationAllocateSerializer


class DesignationAllocationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DesignationAllocation
    serializer_class = serializers.DesignationAllocateSerializer
