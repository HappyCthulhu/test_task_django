
from __future__ import annotations

from random import choices
from string import ascii_letters, digits
from typing import TYPE_CHECKING

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from PIL import Image
from rest_framework.decorators import api_view, parser_classes
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from apps.authentication.models import User
from apps.authentication.serializers.avatar import AvatarSerializer

if TYPE_CHECKING:
    from rest_framework.request import Request


@extend_schema(
    methods=['POST', 'GET'],
    summary="Загрузить новую аватарку или получить аватарку",
    request=AvatarSerializer,
)
@parser_classes([FormParser, MultiPartParser])
@api_view(['POST', 'GET'])
def avatar(request: Request, *_args, **_kwargs) -> Response | HttpResponse:
    assert isinstance(request.user, User)
    user: User = request.user

    if request.method == 'POST':
        serializer = AvatarSerializer(data=request.data)

        assert hasattr(request, 'user')
        serializer.is_valid(raise_exception=True)
        avatar = serializer.validated_data['avatar']

        filename = ''.join(choices(ascii_letters + digits, k=10)) # noqa: S311
        ext = avatar.name.split('.')[-1]

        new_filename = f"{filename}.{ext}"

        image = Image.open(avatar)
        image.thumbnail((200, 200))

        image_path = f"documents/{new_filename}"
        image.save(image_path)

        user.avatar = image_path
        user.save()
        return Response(status=HTTP_201_CREATED)

    if request.method == 'GET':

        if user.avatar:
            response = HttpResponse(user.avatar, content_type='application/octet-stream')
            file_name = user.avatar.name.split('/')[-1]
            file_expr = f'filename="{file_name}"'
            response['Content-Disposition'] = f'attachment; {file_expr}'
            return response
        return HttpResponse(status=HTTP_204_NO_CONTENT)

    assert request.method is not None
    raise MethodNotAllowed(request.method)

