# Generated by Django 4.2.1 on 2023-05-20 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inkling', '0004_document_project_name_remove_project_documents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='project_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='document', to='inkling.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='documents',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inkling.document'),
        ),
    ]