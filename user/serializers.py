from user.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.password = make_password(validated_data.get("password"))
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}










