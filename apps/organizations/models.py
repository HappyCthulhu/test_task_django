from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название организации',
        )
    short_name = models.CharField(
            max_length=255,
            verbose_name='Краткое название организации',
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self) -> str:
        return self.name
