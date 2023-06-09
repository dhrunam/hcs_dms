# Generated by Django 4.0.3 on 2022-09-07 10:50

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex_name', models.CharField(max_length=50, unique=True)),
                ('complex_description', models.CharField(max_length=255)),
                ('complex_isDeleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=40, unique=True)),
                ('department_description', models.CharField(max_length=255)),
                ('department_isDeleted', models.BooleanField()),
                ('department_complex', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.complex')),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=50, unique=True)),
                ('designation_description', models.CharField(max_length=255)),
                ('designation_group', models.CharField(max_length=7)),
                ('designation_isDeleted', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_blood_group',
            field=models.CharField(default='B+', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_contact',
            field=models.CharField(default='9809890987', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_corresponding_address',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_date_of_birth',
            field=models.DateField(default='1977-09-09'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_gender',
            field=models.CharField(default='Male', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_id',
            field=models.CharField(default='EMP001', max_length=12, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_isDeleted',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_permanent_address',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_photo',
            field=models.ImageField(default='', upload_to=accounts.models.get_profile_image_upload_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='employee_type',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DutyAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(auto_now=True)),
                ('to_date', models.DateField(blank=True, default=None, null=True)),
                ('complex_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.complex')),
                ('department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department')),
                ('employee_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DesignationAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(auto_now=True)),
                ('to_date', models.DateField(blank=True, default=None, null=True)),
                ('designation_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.designation')),
                ('employee_id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entry', models.DateField()),
                ('in_time', models.TimeField(blank=True, default=None, null=True)),
                ('out_time', models.TimeField(blank=True, default=None, null=True)),
                ('employee_username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
