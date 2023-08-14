from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.authentication.models import User
from apps.authentication.serializers.user import UserSerializer


class UsersViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
