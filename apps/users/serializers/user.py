from __future__ import annotations

from rest_framework import serializers

from apps.authentication.models import User

model = User

id_ = model.id.field.name
email = model.email.field.name
first_name = model.first_name.field.name
surname = model.surname.field.name
avatar = model.avatar.field.name
phone = model.phone.field.name
organizations = model.organizations.field.name


class UsersSerializer(serializers.ModelSerializer):
    """Controversial decision, but I've been wanting to try it for a while.

    This way, changes in the model field name will be automatically reflected in the serializer.
    """

    class Meta:
        model = model
        fields = (
            id_,
            email,
            first_name,
            surname,
            avatar,
            phone,
            organizations,
        )
