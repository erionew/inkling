# Generated by Django 4.2.1 on 2023-05-20 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inkling', '0007_alter_document_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='documents',
        ),
    ]