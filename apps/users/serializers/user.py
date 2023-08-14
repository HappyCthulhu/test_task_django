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
    """Спорное решение, но давно хотел попробовать.

    Таким образом изменения названия поля модели будут автоматически
    подтягиваться в сериализатор
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
