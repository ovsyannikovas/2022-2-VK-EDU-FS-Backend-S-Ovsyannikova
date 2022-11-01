from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    phone = models.BigIntegerField(unique=True, verbose_name="Номер телефона", null=True)
    username = models.SlugField(max_length=50, unique=True, verbose_name="Ник")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Chat(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=255, null=True, verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Создатель", related_name='author')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", related_name='category')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['id']

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат", related_name='chat')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь", related_name='user')
    content = models.CharField(max_length=255, verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-time_create']
