from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class AttendanceList(generics.ListCreateAPIView):
    queryset = models.Attendance.objects.all().order_by('id')
    serializer_class = serializers.AttendanceSerializer


class AttendanceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Attendance
    serializer_class = serializers.AttendanceSerializer
