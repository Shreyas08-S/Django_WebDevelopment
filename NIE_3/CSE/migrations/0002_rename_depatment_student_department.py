# Generated by Django 5.1.1 on 2024-09-10 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='depatment',
            new_name='department',
        ),
    ]