# Generated by Django 4.0.3 on 2022-09-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_employee_id_userprofile_employee_idxxx'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='employee_idxxx',
            new_name='employee_id',
        ),
    ]
