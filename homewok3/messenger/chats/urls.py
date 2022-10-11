from django.urls import path

from messenger.chats.views import chat_list, create_chat, chat_page

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('chat_page/<name>', chat_page),
    path('create/', create_chat, name='create_chat'),
]