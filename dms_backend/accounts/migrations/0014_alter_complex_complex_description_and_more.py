# Generated by Django 4.0.3 on 2022-09-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_userprofile_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complex',
            name='complex_description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='designation',
            name='designation_description',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
