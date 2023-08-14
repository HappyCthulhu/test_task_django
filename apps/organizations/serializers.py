from rest_framework.serializers import ModelSerializer

from apps.organizations.models import Organization


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'short_name',
        )

        read_only_fields = (
                'id',
                )
