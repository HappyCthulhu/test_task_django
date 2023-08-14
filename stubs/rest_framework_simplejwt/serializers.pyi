from .settings import api_settings as api_settings
from .token_blacklist.models import BlacklistedToken as BlacklistedToken
from .tokens import RefreshToken as RefreshToken, SlidingToken as SlidingToken, UntypedToken as UntypedToken
from _typeshed import Incomplete
from rest_framework import serializers

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs) -> None: ...

class TokenObtainSerializer(serializers.Serializer):
    username_field: Incomplete
    token_class: Incomplete
    default_error_messages: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    user: Incomplete
    def validate(self, attrs): ...
    @classmethod
    def get_token(cls, user): ...

class TokenObtainPairSerializer(TokenObtainSerializer):
    token_class = RefreshToken
    def validate(self, attrs): ...

class TokenObtainSlidingSerializer(TokenObtainSerializer):
    token_class = SlidingToken
    def validate(self, attrs): ...

class TokenRefreshSerializer(serializers.Serializer):
    refresh: Incomplete
    access: Incomplete
    token_class = RefreshToken
    def validate(self, attrs): ...

class TokenRefreshSlidingSerializer(serializers.Serializer):
    token: Incomplete
    token_class = SlidingToken
    def validate(self, attrs): ...

class TokenVerifySerializer(serializers.Serializer):
    token: Incomplete
    def validate(self, attrs): ...

class TokenBlacklistSerializer(serializers.Serializer):
    refresh: Incomplete
    token_class = RefreshToken
    def validate(self, attrs): ...
