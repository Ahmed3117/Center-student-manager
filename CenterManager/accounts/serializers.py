
from rest_framework import serializers

from .models import CustomUser 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name']  # include 'name' field
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            name=validated_data['name']  # set 'name' field
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
