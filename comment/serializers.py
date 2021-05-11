from rest_framework import serializers
from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author_comment = serializers.ReadOnlyField(source='author_comment.username')

    def create(self, validated_data):
        comment = Comments.objects.create(**validated_data)
        comment.save()
        return comment


    class Meta:
        model = Comments
        fields = ['url', 'description', 'author_comment', 'issue_id', 'created_time']