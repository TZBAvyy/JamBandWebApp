# Generated by Django 5.0.2 on 2024-05-22 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bands',
            new_name='Band',
        ),
        migrations.RenameModel(
            old_name='BandMembers',
            new_name='BandMember',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
        migrations.RenameModel(
            old_name='MemberSections',
            new_name='MemberSection',
        ),
        migrations.RenameModel(
            old_name='Practices',
            new_name='Practice',
        ),
        migrations.RenameModel(
            old_name='Sections',
            new_name='Section',
        ),
    ]
