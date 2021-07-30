from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author_comment = serializers.ReadOnlyField(source='author_comment.username')
    issue = serializers.ReadOnlyField(source='issue_id')

    def create(self, validated_data):
        comment = Comments.objects.create(**validated_data)
        comment.save()
        return comment

    class Meta:
        model = Comments
        fields = ['comment_id', 'description', 'author_comment', 'issue', 'created_time']
