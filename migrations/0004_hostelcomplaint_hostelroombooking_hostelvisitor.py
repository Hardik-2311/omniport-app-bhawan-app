# Generated by Django 2.2.3 on 2020-01-27 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_RESIDENCE_MODEL),
        migrations.swappable_dependency(settings.KERNEL_PERSON_MODEL),
        ('bhawan_app', '0003_hostelfacility'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelRoomBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('apr', 'Approved'), ('pen', 'Pending'), ('rej', 'Rejected')], default='pen', max_length=10)),
                ('requested_from', models.DateField()),
                ('requested_till', models.DateField()),
                ('room_no_of_filer', models.PositiveIntegerField()),
                ('filer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_PERSON_MODEL)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_RESIDENCE_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HostelVisitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('relation', models.CharField(max_length=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='bhawan_app.HostelRoomBooking')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HostelComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('complaint_type', models.CharField(choices=[('ele', 'Electric'), ('toi', 'Toilet'), ('car', 'Carpentry'), ('cle', 'Cleaning'), ('oth', 'Other')], default='oth', max_length=10, unique=True)),
                ('status', models.CharField(choices=[('apr', 'Approved'), ('pen', 'Pending'), ('rej', 'Rejected')], default='pen', max_length=10)),
                ('description', models.TextField()),
                ('available_from', models.TimeField()),
                ('available_till', models.TimeField()),
                ('room_no', models.PositiveIntegerField()),
                ('filer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_PERSON_MODEL)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_RESIDENCE_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
