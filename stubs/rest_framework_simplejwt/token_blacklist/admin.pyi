from .models import BlacklistedToken as BlacklistedToken, OutstandingToken as OutstandingToken
from _typeshed import Incomplete
from django.contrib import admin

class OutstandingTokenAdmin(admin.ModelAdmin):
    list_display: Incomplete
    search_fields: Incomplete
    ordering: Incomplete
    def get_queryset(self, *args, **kwargs): ...
    actions: Incomplete
    def get_readonly_fields(self, *args, **kwargs): ...
    def has_add_permission(self, *args, **kwargs): ...
    def has_delete_permission(self, *args, **kwargs): ...
    def has_change_permission(self, request, obj: Incomplete | None = ...): ...

class BlacklistedTokenAdmin(admin.ModelAdmin):
    list_display: Incomplete
    search_fields: Incomplete
    ordering: Incomplete
    def get_queryset(self, *args, **kwargs): ...
    def token_jti(self, obj): ...
    def token_user(self, obj): ...
    def token_created_at(self, obj): ...
    def token_expires_at(self, obj): ...
