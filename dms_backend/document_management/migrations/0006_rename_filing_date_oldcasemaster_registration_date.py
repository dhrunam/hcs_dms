# Generated by Django 4.0.3 on 2022-09-08 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document_management', '0005_oldcasedocument_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oldcasemaster',
            old_name='filing_date',
            new_name='registration_date',
        ),
    ]
