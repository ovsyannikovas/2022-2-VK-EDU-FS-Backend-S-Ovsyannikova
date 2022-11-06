from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('create', views.create_chat, name='create_chat'),
    path('delete', views.delete_chat, name='delete_chat'),
    path('edit_chat', views.edit_chat, name='edit_chat'),
    path('info', views.chat_info, name='chat_info'),
    path('message/send', views.send_message, name='send_message'),
    path('messages', views.chat_messages, name='chat_messages'),
    path('message/mark_read', views.mark_read, name='mark_read'),
    path('message/edit', views.edit_message, name='edit_message'),
    path('message/delete', views.delete_message, name='delete_message'),
]