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


class Chat(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=255, null=True, verbose_name="Описание")
    members = models.ManyToManyField(User, blank=True, default=False, verbose_name="Участники", related_name='members')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['id']

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат", related_name='chat')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь",
                             related_name='user')
    content = models.CharField(max_length=255, verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-time_create']
