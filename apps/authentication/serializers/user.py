from rest_framework import serializers

from apps.authentication.models import User

# TODO: через black прогнать


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'surname',
            'phone',
            'organizations',
            'password',
        )
        read_only_fields = ('id',)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
