# Generated by Django 5.0.2 on 2024-05-22 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_bands_band_rename_bandmembers_bandmember_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='event',
        ),
    ]
