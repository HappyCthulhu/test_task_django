from __future__ import annotations

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email: str, password: str, **extra_fields) -> User:
        if not email:
            msg = 'Email is Required'
            raise ValueError(msg)

        assert isinstance(self.model, User)
        user: User = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> User:
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            msg = 'Superuser must have is_superuser = True'
            raise ValueError(msg)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
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
            )
    phone = models.CharField(
        max_length=12,
        blank=True,
    )
    is_admin = models.BooleanField(
            default=False,
            )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email"]  # noqa: RUF012

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.first_name + self.surname
