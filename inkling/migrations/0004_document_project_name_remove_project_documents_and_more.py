# Generated by Django 4.2.1 on 2023-05-20 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inkling', '0003_remove_document_project_project_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='project_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='document', to='inkling.project'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='documents',
        ),
        migrations.AddField(
            model_name='project',
            name='documents',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inkling.document'),
        ),
    ]
