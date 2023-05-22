# Generated by Django 4.0.3 on 2022-09-16 06:05

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_photo',
            field=models.ImageField(default='', upload_to=accounts.models.get_profile_image_upload_path),
            preserve_default=False,
        ),
    ]