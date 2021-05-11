from user.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedRelatedField(many=True, view_name='projects-detail', read_only=True)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'project', 'password']




