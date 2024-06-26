# Generated by Django 5.0.2 on 2024-06-13 15:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Event name must be greater than 1 character')])),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
            options={
                'ordering': ['date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(help_text='Enter a section (e.g. Bass)', max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Section instrument must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.band')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.event'),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter a member's full name (e.g. Avi)", max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'Member name must be greater than 1 character')])),
                ('bands', models.ManyToManyField(through='display.BandMember', to='display.band')),
            ],
        ),
        migrations.AddField(
            model_name='bandmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.member'),
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(through='display.BandMember', to='display.member'),
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.band')),
            ],
            options={
                'ordering': ['date', 'startTime'],
            },
        ),
        migrations.CreateModel(
            name='MemberSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.IntegerField(choices=[(1, 'Learning'), (2, 'Can Play')])),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.member')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.section')),
            ],
        ),
    ]
