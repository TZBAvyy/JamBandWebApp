# Generated by Django 5.0.2 on 2024-06-24 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_alter_band_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date', '-time']},
        ),
    ]