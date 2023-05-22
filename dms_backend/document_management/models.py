from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
# add the Postgres recommended GIN index
from django.contrib.postgres.indexes import GinIndex
import os


# Create your models here.

def validate_file_extension(value):

    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension. Only PDF files are allowed.')
    else:
        pass


class CaseType(models.Model):
    name = models.CharField(max_length=128, null=False)


class DocumentType(models.Model):
    name = models.CharField(max_length=128, null=False)


class OldCaseMaster(models.Model):

    # pattern of Case ID is  DMS + 4 digit YEAR + 4 digist serial number, ex. DMS20220001,
    case_unique_id = models.CharField(max_length=512, null=False, unique=True)
    case_no = models.CharField(max_length=512, null=False)
    # case_type = models.ForeignKey(
    #     CaseType, on_delete=models.SET_NULL, null=True, related_name='case_type')
    # initial_bench_code = models.CharField(max_length=128, null=True)
    disposal_bench_code = models.CharField(max_length=128, null=True)
    case_year = models.CharField(max_length=4, null=False)
    first_petitioner = models.CharField(max_length=256, null=False)
    first_respondent = models.CharField(max_length=256, null=False)
    additional_petitioner = models.CharField(max_length=2048, null=True)
    additional_respondent = models.CharField(max_length=2048, null=True)
    judge_name = models.CharField(max_length=512, null=True)
    petitioner_counsel = models.CharField(max_length=2048, null=True)
    respondent_counsel = models.CharField(max_length=2048, null=True)
    district = models.CharField(max_length=32, null=True)
    registration_date = models.DateField()
    disposal_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='data_entry_approved_by')
    approval_date = models.DateField(null=True)
    approval_remarks = models.CharField(
        max_length=1028, null=True, default='', blank=True)
    # document_url = models.CharField(max_length=1024, null=True)
    # field for utilize tsvector for full text search
    search_vector = SearchVectorField(null=True)

    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='case_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='case_updated_by')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['case_no=' + str(self.case_no), 'first_petitioner=' + self.first_petitioner, 'first_respondent=' + self.first_respondent])

    class Meta:

        indexes = (GinIndex(fields=["search_vector"]),)  # add index


def get_old_case_document_upload_path(instance, filename):

    document_type = DocumentType.objects.get(id=instance.type_id.id)
    case = OldCaseMaster.objects.get(id=instance.case_id.id)
    path = os.path.join(
        "old_case", case.case_no.replace('/', '_'), document_type.name, filename)
    print(path)
    return path


class OldCaseDocument(models.Model):
    case_id = models.ForeignKey(
        OldCaseMaster, on_delete=models.SET_NULL, null=True, related_name="related_case")
    type_id = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, null=True, related_name="related_type")
    document_url = models.FileField(
        upload_to=get_old_case_document_upload_path, validators=[validate_file_extension])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class NewCaseMaster(models.Model):

    # pattern of Case ID is  DMS + 4 digit YEAR + 4 digist serial number, ex. DMS20220001,
    case_unique_id = models.CharField(max_length=512, null=False, unique=True)
    case_no = models.CharField(max_length=512, null=False)
    # case_type = models.ForeignKey(
    #     CaseType, on_delete=models.SET_NULL, null=True, related_name='case_type')
    # initial_bench_code = models.CharField(max_length=128, null=True)
    disposal_bench_code = models.CharField(max_length=128, null=True)
    case_year = models.CharField(max_length=4, null=False)
    first_petitioner = models.CharField(max_length=256, null=False)
    first_respondent = models.CharField(max_length=256, null=False)
    additional_petitioner = models.CharField(max_length=1024, null=True)
    additional_respondent = models.CharField(max_length=1024, null=True)
    judge_name = models.CharField(max_length=256, null=True)
    petitioner_counsel = models.CharField(max_length=1024, null=True)
    respondent_counsel = models.CharField(max_length=1024, null=True)
    district = models.CharField(max_length=32, null=True)
    registration_date = models.DateField()
    disposal_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='new_case_data_entry_approved_by')
    approval_date = models.DateField(null=True)
    approval_remarks = models.CharField(
        max_length=1028, null=True, default='', blank=True)
    # document_url = models.CharField(max_length=1024, null=True)
    # field for utilize tsvector for full text search
    search_vector = SearchVectorField(null=True)

    created_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='new_case_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='new_case_updated_by')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['case_no=' + str(self.case_no), 'first_petitioner=' + self.first_petitioner, 'first_respondent=' + self.first_respondent])

    class Meta:

        indexes = (GinIndex(fields=["search_vector"]),)  # add index


def get_new_case_document_upload_path(instance, filename):

    document_type = DocumentType.objects.get(id=instance.type_id.id)
    case = NewCaseMaster.objects.get(id=instance.case_id.id)
    path = os.path.join(
        "new_case", case.case_no.replace('/', '_'), document_type.name, filename)
    print(path)
    return path


class NewCaseDocument(models.Model):
    case_id = models.ForeignKey(
        NewCaseMaster, on_delete=models.SET_NULL, null=True, related_name="new_related_case")
    type_id = models.ForeignKey(
        DocumentType, on_delete=models.SET_NULL, null=True, related_name="new_related_type")
    document_url = models.FileField(
        upload_to=get_new_case_document_upload_path, validators=[validate_file_extension])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
