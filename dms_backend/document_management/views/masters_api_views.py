
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group

from accounts import serializers, models
from durin.auth import TokenAuthentication
from document_management import models
from document_management import serializers as dms_serializers


class DocumentTypeList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.DocumentType.objects.all().order_by('id')
    serializer_class = dms_serializers.DocumentTypeSerializer


class DocumentTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.DocumentType
    serializer_class = dms_serializers.DocumentTypeSerializer


class CaseTypeList(generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.CaseType.objects.all().order_by('id')
    serializer_class = dms_serializers.CaseTypeSerializer


class CaseTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = models.CaseType
    serializer_class = dms_serializers.CaseTypeSerializer
