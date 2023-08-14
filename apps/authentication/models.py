from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from apps.organizations.models import Organization


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email: str, password: str, **extra_fields) -> User:
        if not email:
            msg = 'Email is Required'
            raise ValueError(msg)

        user: User = self.model(email=self.normalize_email(email), **extra_fields)  # type: ignore # noqa: PGH003
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> User:
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            msg = 'Superuser must have is_superuser = True'
            raise ValueError(msg)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
    )
    surname = models.CharField(
        max_length=255,
        blank=True,
    )
    avatar = models.FileField(
        max_length=4096,
        upload_to="documents",
        verbose_name="Файл",
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
    )

    organizations = models.ManyToManyField(
        Organization,
        verbose_name="Организации",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def is_staff(self) -> bool:
        return self.is_superuser

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.first_name + self.surname
