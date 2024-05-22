# Generated by Django 5.0.2 on 2024-05-22 01:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter a member's full name (e.g. Avi)", max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Member name must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(help_text='Enter a section (e.g. Bass)', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Section instrument must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Bands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.events')),
            ],
        ),
        migrations.CreateModel(
            name='Practices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bands')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.events')),
            ],
        ),
        migrations.CreateModel(
            name='MemberSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Novice'), (3, 'Adept'), (4, 'Skilled'), (5, 'Expert')])),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.members')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sections')),
            ],
        ),
        migrations.CreateModel(
            name='BandMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bands')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.members')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.sections')),
            ],
        ),
    ]