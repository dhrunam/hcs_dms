# Generated by Django 4.0.3 on 2022-09-06 10:49

from django.conf import settings
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OldCaseMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('case_unique_id', models.CharField(max_length=512, unique=True)),
                ('case_no', models.CharField(max_length=512)),
                ('disposal_bench_code', models.CharField(max_length=128, null=True)),
                ('case_year', models.CharField(max_length=4)),
                ('first_petitioner', models.CharField(max_length=256)),
                ('first_respondent', models.CharField(max_length=256)),
                ('additional_petitioner', models.CharField(
                    max_length=1024, null=True)),
                ('additional_respondent', models.CharField(
                    max_length=1024, null=True)),
                ('judge_name', models.CharField(max_length=256, null=True)),
                ('petitioner_counsel', models.CharField(max_length=128, null=True)),
                ('respondent_counsel', models.CharField(max_length=128, null=True)),
                ('district', models.CharField(max_length=32, null=True)),
                ('filing_date', models.DateField()),
                ('disposal_date', models.DateField()),
                ('vector_column',
                 django.contrib.postgres.search.SearchVectorField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='case_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='case_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OldCaseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('document_url', models.FileField(upload_to='old_case')),
                ('case_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='related_case', to='document_management.oldcasemaster')),
                ('type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                 related_name='related_type', to='document_management.documenttype')),
            ],
        ),
        migrations.AddIndex(
            model_name='oldcasemaster',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=['vector_column'], name='document_ma_vector__b1d8c6_gin'),
        ),
    ]