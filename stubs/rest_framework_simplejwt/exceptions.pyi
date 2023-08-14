from _typeshed import Incomplete
from rest_framework import exceptions

class TokenError(Exception): ...
class TokenBackendError(Exception): ...

class DetailDictMixin:
    def __init__(self, detail: Incomplete | None = ..., code: Incomplete | None = ...) -> None: ...

class AuthenticationFailed(DetailDictMixin, exceptions.AuthenticationFailed): ...

class InvalidToken(AuthenticationFailed):
    status_code: Incomplete
    default_detail: Incomplete
    default_code: str
