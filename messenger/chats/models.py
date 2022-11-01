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


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # ordering = ['id']


class Chat(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    description = models.CharField(max_length=255, null=True, verbose_name="Описание")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Создатель")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name="Чат")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")
    content = models.CharField(max_length=255, verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
