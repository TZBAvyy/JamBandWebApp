# Generated by Django 5.0.2 on 2024-05-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0005_remove_bandmember_member_remove_bandmember_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersection',
            name='proficiency',
            field=models.IntegerField(choices=[(1, 'Learning'), (2, 'Can Play')]),
        ),
    ]
