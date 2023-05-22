from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class DutyAllocationList(generics.ListCreateAPIView):
    queryset = models.DutyAllocation.objects.all().order_by('id')
    serializer_class = serializers.DutyAllocationSerializer


class DutyAllocationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DutyAllocation
    serializer_class = serializers.DutyAllocationSerializer
