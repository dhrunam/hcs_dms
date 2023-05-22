# Generated by Django 4.0.3 on 2022-09-12 09:07

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_merge_20220912_0905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='employee_idxx',
            new_name='employee_id',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='employee_photo',
            field=models.ImageField(null=True, upload_to=accounts.models.get_profile_image_upload_path),
        ),
    ]
