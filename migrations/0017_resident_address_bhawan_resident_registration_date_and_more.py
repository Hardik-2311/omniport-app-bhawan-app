# Generated by Django 4.1.5 on 2024-08-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhawan_app', '0016_auto_20221116_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='address_bhawan',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='resident',
            name='registration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('res', 'Resolved'), ('pen', 'Pending'), ('unr', 'Unresolved'), ('ipr', 'Inprocess')], default='pen', max_length=10),
        ),
    ]