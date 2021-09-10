from rest_framework import serializers
from .models import Issues


class IssueSerializer(serializers.ModelSerializer):
    author_issue = serializers.ReadOnlyField(source='author_issue.username')
    project = serializers.ReadOnlyField(source='project.id')

    def create(self, validated_data):
        issue = Issues.objects.create(**validated_data)
        issue.save()
        return issue

    class Meta:
        model = Issues
        fields = ['id', 'url', 'title', 'desc', 'project', 'tag', 'priority', 'status',
                  'author_issue', 'assignee_user_id', 'create_time']
