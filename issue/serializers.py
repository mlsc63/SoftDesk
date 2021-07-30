from rest_framework import serializers
from .models import Issues


class IssueSerializer(serializers.ModelSerializer):
    author_issue = serializers.ReadOnlyField(source='author_issue.username')
    comment = serializers.HyperlinkedRelatedField(many=True, view_name='comments-detail', read_only=True)
    project = serializers.ReadOnlyField(source='project_id')

    def create(self, validated_data):
        print(str(validated_data))
        issue = Issues.objects.create(**validated_data)
        issue.save()
        return issue


    class Meta:
        model = Issues
        fields = ['issue_id', 'project', 'url', 'title', 'desc', 'project_id', 'tag', 'priority', 'status',
                  'author_issue', 'assignee_user_id', 'create_time', 'comment']