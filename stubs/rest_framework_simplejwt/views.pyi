from . import serializers as serializers
from .authentication import AUTH_HEADER_TYPES as AUTH_HEADER_TYPES
from .exceptions import InvalidToken as InvalidToken, TokenError as TokenError
from .settings import api_settings as api_settings
from _typeshed import Incomplete
from rest_framework import generics

class TokenViewBase(generics.GenericAPIView):
    permission_classes: Incomplete
    authentication_classes: Incomplete
    serializer_class: Incomplete
    www_authenticate_realm: str
    def get_serializer_class(self): ...
    def get_authenticate_header(self, request): ...
    def post(self, request, *args, **kwargs): ...

class TokenObtainPairView(TokenViewBase): ...

token_obtain_pair: Incomplete

class TokenRefreshView(TokenViewBase): ...

token_refresh: Incomplete

class TokenObtainSlidingView(TokenViewBase): ...

token_obtain_sliding: Incomplete

class TokenRefreshSlidingView(TokenViewBase): ...

token_refresh_sliding: Incomplete

class TokenVerifyView(TokenViewBase): ...

token_verify: Incomplete

class TokenBlacklistView(TokenViewBase): ...

token_blacklist: Incomplete
