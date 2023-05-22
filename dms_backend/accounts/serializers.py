from rest_framework import serializers
from accounts import models as acc_model
from django.contrib.auth.models import (User, Group)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction, connection
# from configuration.serializers import (
#     DesignationSerializer,
#     OfficeSerializer
# )


class UserGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group

        fields = [
            'id',
            'name',

        ]


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.UserProfile

        fields = [
            'id',
            'user',
            'employee_id',
            'employee_name',
            'employee_type',
            'employee_gender',
            'employee_blood_group',
            'employee_date_of_birth',
            'employee_corresponding_address',
            'employee_permanent_address',
            'employee_contact',
            'employee_photo',
            'employee_isDeleted',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',

        ]


class ResgisteredUserSerializer(serializers.ModelSerializer):
    related_profile = UserProfileSerializer(many=False, read_only=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'password2',
            'last_login',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
            'related_profile',

        ]

    # def update(self, instance, validated_data):

    #     try:
    #         # with transaction.atomic():
    #         profile = instance
    #         # user.email = validated_data['email']
    #         # user.first_name = validated_data['first_name']
    #         # user.last_name = validated_data['last_name']
    #         # user.is_staff = True if validated_data['group'] == 'user' else False

    #         profile.save()

    #         return user

    #     except TypeError:
    #         return TypeError("There is some error in processing your data.")


class ResgisteredUserPatchSerializer(serializers.ModelSerializer):
    related_profile = UserProfileSerializer(many=False, read_only=True)
    password = serializers.CharField(
        write_only=True, required=False, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=False)

    group = serializers.CharField(
        max_length=128, write_only=True, required=False)
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'password2',
            'last_login',
            'is_superuser',
            'first_name',
            'last_name',
            'email',
            'group',
            'is_staff',
            'is_active',
            'date_joined',
            'related_profile',

        ]

    def update(self, instance, validated_data):
        print(validated_data)
        print(validated_data.get('group'))
        try:
            with transaction.atomic(using='dms'):
                user = instance
                # user.email = validated_data['email']
                # user.first_name = validated_data['first_name']
                # user.last_name = validated_data['last_name']
                # user.is_staff = True if validated_data['group'] == 'user' else False
                if validated_data.get('password') is not None:
                    user.set_password(validated_data['password'])
                # if validated_data.get('group') is not None:
                #     user.groups.add(Group.objects.get(
                #         id=validated_data['group']))
                instance.groups.clear()

                user.groups.add(Group.objects.get(
                    id=validated_data.get('group')))
                if validated_data.get('email') is not None:
                    user.email = validated_data.get('email')
                user.save()

            return user

        except TypeError:
            return TypeError("There is some error in processing your data.")


class RegisterSerializer(serializers.ModelSerializer):
    related_profile = UserProfileSerializer(many=False, read_only=True)
    related_groups = UserGroupSerializer(
        source='groups',  many=True, read_only=True)
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # email=serializers.CharField(write_only=True, max_length=128)
    first_name = serializers.CharField(max_length=128, required=False)
    last_name = serializers.CharField(max_length=128, required=False)
    # designation = serializers.IntegerField(write_only=True, required=True)
    # office = serializers.IntegerField(write_only=True, required=True)
    # contact_number = serializers.CharField(write_only=True, max_length=12)
    # is_staff = serializers.BooleanField(default=False)
    group = serializers.CharField(max_length=128, write_only=True)

    employee_id = serializers.CharField(
        max_length=12, required=False)
    employee_name = serializers.CharField(
        max_length=128, required=False)
    employee_type = serializers.CharField(max_length=12, required=False)
    employee_gender = serializers.CharField(max_length=6, required=False)
    employee_blood_group = serializers.CharField(max_length=6, required=False)
    employee_date_of_birth = serializers.DateField(required=False)
    employee_corresponding_address = serializers.CharField(
        max_length=1024, required=False)
    employee_permanent_address = serializers.CharField(
        max_length=1024, required=False)
    employee_contact = serializers.CharField(max_length=10, required=False)
    employee_photo = serializers.ImageField(required=False)
    employee_isDeleted = serializers.BooleanField(required=False)

    created_by = serializers.IntegerField(required=False)
    updated_by = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password', 'password2',
            'email',
            'first_name',
            'last_name',
            'group',
            'employee_name',
            'employee_blood_group',
            'employee_contact',
            'employee_corresponding_address',
            'employee_date_of_birth',
            'employee_gender',
            'employee_isDeleted',
            'employee_permanent_address',
            'employee_photo',
            'employee_type',
            'employee_id',
            'created_by',
            'updated_by',
            'related_profile',
            'related_groups'
        ]
        # extra_kwargs = {
        #     'first_name': {'required': False},
        #     'last_name': {'required': False},
        #     'created_by': {'required': False},
        #     'updated_by': {'required': False}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        try:
            with transaction.atomic(using='dms'):
                # if validated_data.get('employee_photo') is not None:
                #     photo = validated_data['employee_photo']
                # else:
                #     photo = ''
                user = User.objects.create(
                    username=validated_data.get('username'),
                    email=validated_data.get('email'),
                    # first_name=validated_data['first_name'],
                    # last_name=validated_data['last_name'],
                    is_staff=True if validated_data.get(
                        'group') == 'user' else False,
                )
                user.groups.add(Group.objects.get(
                    id=validated_data.get('group')))
                user.set_password(validated_data.get('password'))
                user.save()
                user_profile = acc_model.UserProfile.objects.update_or_create(
                    user=user,
                    defaults={
                        "employee_id": validated_data.get('employee_id'),
                        "employee_name": validated_data.get('employee_name'),
                        "employee_type": validated_data.get('employee_type'),
                        "employee_gender": validated_data.get('employee_gender'),
                        "employee_blood_group": validated_data.get('employee_blood_group'),
                        "employee_date_of_birth": validated_data.get('employee_date_of_birth'),
                        "employee_corresponding_address": validated_data.get('employee_corresponding_address'),
                        "employee_permanent_address": validated_data.get('employee_permanent_address'),
                        "employee_contact": validated_data.get('employee_contact'),
                        "employee_photo": validated_data.get('employee_photo'),
                        "employee_isDeleted": validated_data.get('employee_isDeleted'),
                        "created_by": User.objects.get(id=validated_data.get('created_by')),
                        "updated_by": User.objects.get(id=validated_data.get('updated_by')),
                    }

                )

            return user

        except TypeError:
            return TypeError("There is some error in processing your data.")

    def initialize_profile(validated_data):

        profile = {}
        if validated_data.get('employee_type') is not None:
            profile.add('employee_type', validated_data.get('employee_type'))

        return profile

    def update(self, instance, validated_data):

        try:
            with transaction.atomic(using='dms'):
                user = instance

                user.username = validated_data.get('username')
                user.email = validated_data.get('email')
                user.first_name = validated_data.get('first_name')
                user.last_name = validated_data.get('last_name')
                user.is_staff = True if validated_data.get(
                    'group') == 'user' else False
                user.set_password(validated_data.get('password'))
                user.groups.add(Group.objects.get(
                    name=validated_data.get('group')))
                user.save()

                user_profile = acc_model.UserProfile.objects.update_or_create(
                    user=user,
                    defaults={
                        "employee_id": validated_data.get('employee_id'),
                        "employee_type": validated_data.get('employee_type'),
                        "employee_gender": validated_data.get('employee_gender'),
                        "employee_blood_group": validated_data.get('employee_blood_group'),
                        "employee_date_of_birth": validated_data.get('employee_date_of_birth'),
                        "employee_corresponding_address": validated_data.get('employee_corresponding_address'),
                        "employee_permanent_address": validated_data.get('employee_permanent_address'),
                        "employee_contact": validated_data.get('employee_contact'),
                        "employee_photo": validated_data.get('employee_photo'),
                        "employee_isDeleted": validated_data.get('employee_isDeleted'),
                        "created_by": User.objects.get(id=validated_data.get('created_by')),
                        "updated_by": User.objects.get(id=validated_data.get('updated_by')),
                    }

                )

            return user

        except TypeError:
            return TypeError("There is some error in processing your data.")


class LeanUserSerializer(serializers.ModelSerializer):
    related_profile = UserProfileSerializer(many=False, read_only=True)
    related_groups = UserGroupSerializer(
        source='groups',  many=True, read_only=True)

    class Meta:
        model = User

        fields = [

            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'related_profile',
            'is_staff',
            'related_groups'

        ]


class ComplexSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.Complex
        fields = (
            'id',
            'complex_name',
            'complex_description',
            'complex_isDeleted'
        )


class DepartmentSerializer(serializers.ModelSerializer):
    related_complex = ComplexSerializer(
        source='department_complex', read_only=True)

    class Meta:
        model = acc_model.Department
        fields = (
            'id',
            'department_name',
            'department_description',
            'department_complex',
            'department_isDeleted',
            'related_complex'
        )


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.Designation
        fields = (
            'id',
            'designation_name',
            'designation_description',
            'designation_group',
            'designation_isDeleted'
        )


class DesignationAllocateSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.DesignationAllocation
        fields = (
            'id',
            'employee_id',
            'designation_id',
            'from_date',
            'to_date',
        )


class DutyAllocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.DutyAllocation
        fields = (
            'id',
            'employee_id',
            'complex_id',
            'department_id',
            'from_date',
            'to_date'
        )


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_model.Attendance
        fields = (
            'employee_username',
            'date',
            'in_time',
            'out_time',
        )
