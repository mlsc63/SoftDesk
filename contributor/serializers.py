from .models import Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        contributor = Contributor.objects.create(**validated_data)
        contributor.save()
        return contributor

    class Meta:
        model = Contributor
        fields = ['url', 'user_id', 'project_id', 'permission', 'role']

