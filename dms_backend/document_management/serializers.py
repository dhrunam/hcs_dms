from rest_framework import serializers
from accounts import models as acc_model
from django.contrib.auth.models import (User, Group)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction, connection
from document_management.models import(
    DocumentType,
    CaseType,
    OldCaseDocument,
    OldCaseMaster,
    NewCaseDocument,
    NewCaseMaster,

)

from accounts.serializers import (
    ResgisteredUserSerializer,
)


class CaseTypeSerializer(serializers.ModelSerializer):
    # related_accounthead = AccountHeadSerializer(
    #     source="account_head", read_only=True)
    # related_create_user = ResgisteredUserSerializer(
    #     source='created_by', read_only=True)
    # related_update_user = ResgisteredUserSerializer(
    #     source='updated_by', read_only=True)

    class Meta:
        model = CaseType

        fields = [
            'id',
            'name',
        ]


class DocumentTypeSerializer(serializers.ModelSerializer):
    # related_accounthead = AccountHeadSerializer(
    #     source="account_head", read_only=True)
    # related_create_user = ResgisteredUserSerializer(
    #     source='created_by', read_only=True)
    # related_update_user = ResgisteredUserSerializer(
    #     source='updated_by', read_only=True)

    class Meta:
        model = DocumentType

        fields = [
            'id',
            'name',
        ]


class OldCaseDocumentSerializers(serializers.ModelSerializer):
    related_type = DocumentTypeSerializer(source='type_id', read_only=True)

    class Meta:
        model = OldCaseDocument
        fields = [
            'id',
            'document_url',
            'case_id',
            'type_id',
            'related_type'

        ]


class OldCaseMasterSerializers(serializers.ModelSerializer):

    related_documents = OldCaseDocumentSerializers(
        source='related_case', many=True, read_only=True)
    # judge_name = serializers.CharField(
    #     required=False, default='')
    additional_petitioner = serializers.CharField(
        required=False, default='')
    additional_respondent = serializers.CharField(
        required=False, default='')
    # petitioner_counsel = serializers.CharField(
    #     required=False, default='')
    # respondent_counsel = serializers.CharField(
    #     required=False, default='')
    # district = serializers.CharField(
    #     required=False, default='')

    class Meta:
        model = OldCaseMaster

        fields = [
            'id',
            'case_no',
            'disposal_bench_code',
            'case_year',
            'first_petitioner',
            'first_respondent',
            'additional_petitioner',
            'additional_respondent',
            'judge_name',
            'petitioner_counsel',
            'respondent_counsel',
            'district',
            'registration_date',
            'disposal_date',
            'search_vector',
            'is_approved',
            'approved_by',
            'approval_date',
            'approval_remarks',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'case_unique_id',
            'related_documents'
        ]


class NewCaseDocumentSerializers(serializers.ModelSerializer):
    related_type = DocumentTypeSerializer(source='type_id', read_only=True)

    class Meta:
        model = NewCaseDocument
        fields = [
            'id',
            'document_url',
            'case_id',
            'type_id',
            'related_type'

        ]


class NewCaseMasterSerializers(serializers.ModelSerializer):

    related_documents = NewCaseDocumentSerializers(
        source='new_related_case', many=True, read_only=True)
    # judge_name = serializers.CharField(
    #     required=False, default='')
    additional_petitioner = serializers.CharField(
        required=False, default='')
    additional_respondent = serializers.CharField(
        required=False, default='')
    # petitioner_counsel = serializers.CharField(
    #     required=False, default='')
    # respondent_counsel = serializers.CharField(
    #     required=False, default='')
    # district = serializers.CharField(
    #     required=False, default='')

    class Meta:
        model = NewCaseMaster

        fields = [
            'id',
            'case_no',
            'disposal_bench_code',
            'case_year',
            'first_petitioner',
            'first_respondent',
            'additional_petitioner',
            'additional_respondent',
            'judge_name',
            'petitioner_counsel',
            'respondent_counsel',
            'district',
            'registration_date',
            'disposal_date',
            'search_vector',
            'is_approved',
            'approved_by',
            'approval_date',
            'approval_remarks',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'case_unique_id',
            'related_documents'
        ]
