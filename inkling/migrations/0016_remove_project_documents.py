# Generated by Django 4.2.1 on 2023-05-20 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inkling', '0015_alter_document_project_name_remove_project_documents_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='documents',
        ),
    ]
