from .models import Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.id')

    def create(self, validated_data):
        print('create')
        contributor = Contributor.objects.create(**validated_data)
        contributor.save()
        return contributor

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project', 'permission', 'role']
