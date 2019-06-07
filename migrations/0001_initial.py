# Generated by Django 2.2 on 2019-06-07 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import formula_one.utils.upload_to


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_RESIDENCE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('display_picture', models.ImageField(upload_to=formula_one.utils.upload_to.UploadTo('bhawan_app', 'hostel'))),
                ('homepage_url', models.URLField(blank=True, verbose_name='Homepage URL')),
                ('hostel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_RESIDENCE_MODEL)),
            ],
            options={
                'verbose_name_plural': 'hostel profile',
            },
        ),
    ]
