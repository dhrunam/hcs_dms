# Generated by Django 4.0.3 on 2022-09-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_management', '0004_alter_oldcasedocument_document_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldcasedocument',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-03-05'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oldcasedocument',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default='2022-03-5'),
            preserve_default=False,
        ),
    ]
