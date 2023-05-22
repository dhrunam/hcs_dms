import os
from turtle import update
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# import magic


# def get_mime_type(file):
#     """
#     Get MIME by reading the header of the file
#     """
#     initial_pos = file.tell()
#     file.seek(0)
#     mime_type = magic.from_buffer(file.read(2048), mime=True)
#     file.seek(initial_pos)
#     print(mime_type)
#     return mime_type


# Create your models here.


def validate_file_extension(value):

    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension. Only PDF files are allowed.')


def get_profile_image_upload_path(instance, filename):

    path = os.path.join(
        "profile_image", instance.user.username, filename)

    return path


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name='related_profile')
    employee_id = models.CharField(max_length=12, blank=False, unique=True)
    employee_name = models.CharField(max_length=128, blank=False)
    employee_type = models.CharField(max_length=12, blank=False)
    employee_gender = models.CharField(max_length=6, blank=False)
    employee_blood_group = models.CharField(max_length=6)
    employee_date_of_birth = models.DateField(blank=False)
    employee_corresponding_address = models.CharField(
        max_length=1024, blank=False)
    employee_permanent_address = models.CharField(max_length=1024, blank=False)
    employee_contact = models.CharField(max_length=10, blank=False)
    employee_photo = models.ImageField(
        upload_to=get_profile_image_upload_path)
    employee_isDeleted = models.BooleanField(blank=False, default=False)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='profile_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='profile_updated_by')
    updated_at = models.DateTimeField(auto_now_add=True)

# From One Stop Slution


class Complex(models.Model):
    complex_name = models.CharField(max_length=50, blank=False, unique=True)
    complex_description = models.TextField(max_length=255, blank=True)
    complex_isDeleted = models.BooleanField(blank=False)


class Designation(models.Model):
    designation_name = models.CharField(
        max_length=50, blank=False, unique=True)
    designation_description = models.TextField(max_length=255, blank=True)
    designation_group = models.CharField(max_length=7, blank=False)
    designation_isDeleted = models.BooleanField(blank=False, default=False)


class Department(models.Model):
    department_name = models.CharField(max_length=40, blank=False, unique=True)
    department_description = models.TextField(max_length=255, blank=True)
    department_isDeleted = models.BooleanField()
    department_complex = models.ForeignKey(
        Complex, default=None, on_delete=models.CASCADE)


class DesignationAllocation(models.Model):
    employee_id = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(
        Designation, default=None, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField(blank=True, default=None, null=True)


class DutyAllocation(models.Model):
    employee_id = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    complex_id = models.ForeignKey(
        Complex, default=None, on_delete=models.CASCADE)
    department_id = models.ForeignKey(
        Department, null=True, blank=True, on_delete=models.SET_NULL)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField(blank=True, default=None, null=True)


class Attendance(models.Model):
    employee_username = models.ForeignKey(
        UserProfile, default=None, on_delete=models.CASCADE)
    date_entry = models.DateField(blank=False)
    in_time = models.TimeField(blank=True, null=True, default=None)
    out_time = models.TimeField(blank=True, null=True, default=None)
