from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.serializers.registration import RegistrationSerializer


# view for registering users
class RegisterView(APIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
