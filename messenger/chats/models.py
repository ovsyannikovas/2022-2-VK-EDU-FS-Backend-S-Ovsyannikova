from django.db import models
from users.models import User


class Chat(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=255, null=True, verbose_name="Описание")
    members = models.ManyToManyField(User, blank=True, verbose_name="Участники", related_name='members')

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
    mark = models.BooleanField(default=False, verbose_name="Пометка прочитанности")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['time_create']
