from .models import Contributor
from rest_framework import serializers


class ContributorSerializer(serializers.ModelSerializer):
    project_id_contributor = serializers.ReadOnlyField(source='project_id')


    def create(self, validated_data):

        print(str(validated_data))
        contributor = Contributor.objects.create(**validated_data)
        contributor.save()
        return contributor

    class Meta:
        model = Contributor
        fields = ['contributor_id', 'user_id', 'project_id_contributor', 'permission', 'role']

