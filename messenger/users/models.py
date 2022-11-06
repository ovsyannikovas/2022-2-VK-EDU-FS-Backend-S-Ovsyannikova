from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.BigIntegerField(unique=True, verbose_name="Номер телефона", null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username
