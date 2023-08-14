from rest_framework import serializers

from apps.authentication.models import User


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)
