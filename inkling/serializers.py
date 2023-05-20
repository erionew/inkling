from rest_framework import serializers

from .models import Project, Document

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedRelatedField(
        view_name='document_detail',
        many = True,
        read_only=True,
    )
    class Meta:
        model = Project
        fields = ('id', 'name', 'documents')

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset = Project.objects.all())

    class Meta:
        model = Document
        fields = ('id', 'title', 'project')