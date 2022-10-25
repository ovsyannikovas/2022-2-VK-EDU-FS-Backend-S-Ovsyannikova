from django.contrib import admin

from .models import Chat, Category, Message

admin.site.register(Chat)
admin.site.register(Category)
admin.site.register(Message)
