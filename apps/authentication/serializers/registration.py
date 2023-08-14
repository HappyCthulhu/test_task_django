from __future__ import annotations

from typing import ClassVar

from rest_framework import serializers

from apps.authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
        )
        extra_kwargs: ClassVar[dict[str, dict[str, bool]]] = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data: dict) -> User:
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
