from .exceptions import TokenBackendError as TokenBackendError, TokenError as TokenError
from .settings import api_settings as api_settings
from .token_blacklist.models import BlacklistedToken as BlacklistedToken, OutstandingToken as OutstandingToken
from .utils import aware_utcnow as aware_utcnow, datetime_from_epoch as datetime_from_epoch, datetime_to_epoch as datetime_to_epoch, format_lazy as format_lazy
from _typeshed import Incomplete

class Token:
    token_type: Incomplete
    lifetime: Incomplete
    token: Incomplete
    current_time: Incomplete
    payload: Incomplete
    def __init__(self, token: Incomplete | None = ..., verify: bool = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, default: Incomplete | None = ...): ...
    def verify(self) -> None: ...
    def verify_token_type(self) -> None: ...
    def set_jti(self) -> None: ...
    def set_exp(self, claim: str = ..., from_time: Incomplete | None = ..., lifetime: Incomplete | None = ...) -> None: ...
    def set_iat(self, claim: str = ..., at_time: Incomplete | None = ...) -> None: ...
    def check_exp(self, claim: str = ..., current_time: Incomplete | None = ...) -> None: ...
    @classmethod
    def for_user(cls, user): ...
    @property
    def token_backend(self): ...
    def get_token_backend(self): ...

class BlacklistMixin:
    def verify(self, *args, **kwargs) -> None: ...
    def check_blacklist(self) -> None: ...
    def blacklist(self): ...
    @classmethod
    def for_user(cls, user): ...

class SlidingToken(BlacklistMixin, Token):
    token_type: str
    lifetime: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

class AccessToken(Token):
    token_type: str
    lifetime: Incomplete

class RefreshToken(BlacklistMixin, Token):
    token_type: str
    lifetime: Incomplete
    no_copy_claims: Incomplete
    access_token_class = AccessToken
    @property
    def access_token(self): ...

class UntypedToken(Token):
    token_type: str
    lifetime: Incomplete
    def verify_token_type(self) -> None: ...
