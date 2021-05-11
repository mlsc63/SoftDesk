from .models import Projects
from rest_framework import serializers




class ProjectSerializer(serializers.ModelSerializer):
    author_project = serializers.ReadOnlyField(source='author_project.username')
    issue = serializers.HyperlinkedRelatedField(many=True, view_name='issues-detail', read_only=True)

    def create(self, validated_data):
        project = Projects.objects.create(**validated_data)
        project.save()
        return project


    class Meta:
        model = Projects
        fields = ['url', 'title', 'description', 'type', 'author_project', 'issue']

