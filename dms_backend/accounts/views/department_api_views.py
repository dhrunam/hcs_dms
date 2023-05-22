
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication


class DepartmentList(generics.ListCreateAPIView):
    queryset = models.Department.objects.all().order_by('id')
    serializer_class = serializers.DepartmentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases item  received
        for the specified order .
        """
        complex_id = self.request.query_params.get('complex_id')
        if complex_id:
            return self.queryset.filter(department_complex=complex_id).order_by('id')
        return self.queryset


class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Department
    serializer_class = serializers.DepartmentSerializer
