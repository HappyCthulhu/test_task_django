import json
from .exceptions import TokenBackendError as TokenBackendError
from .utils import format_lazy as format_lazy
from _typeshed import Incomplete
from datetime import timedelta
from typing import Optional, Type, Union

JWK_CLIENT_AVAILABLE: bool
ALLOWED_ALGORITHMS: Incomplete

class TokenBackend:
    algorithm: Incomplete
    signing_key: Incomplete
    verifying_key: Incomplete
    audience: Incomplete
    issuer: Incomplete
    jwks_client: Incomplete
    leeway: Incomplete
    json_encoder: Incomplete
    def __init__(self, algorithm, signing_key: Incomplete | None = ..., verifying_key: str = ..., audience: Incomplete | None = ..., issuer: Incomplete | None = ..., jwk_url: str = ..., leeway: Union[float, int, timedelta] = ..., json_encoder: Optional[Type[json.JSONEncoder]] = ...) -> None: ...
    def get_leeway(self) -> timedelta: ...
    def get_verifying_key(self, token): ...
    def encode(self, payload): ...
    def decode(self, token, verify: bool = ...): ...
