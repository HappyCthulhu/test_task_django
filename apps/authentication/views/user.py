from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.users.serializers.user import UsersSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UsersSerializer

    def retrieve(self, request: Request, *_args, **_kwargs) -> Response:
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)

    def update(self, request: Request, *_args, **_kwargs) -> Response:
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, *_args, **_kwargs) -> Response:
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
