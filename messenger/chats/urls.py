from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    # path('chat_page/<chat_id>', views.chat_page),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('delete_chat/', views.delete_chat, name='delete_chat'),
    path('add_member/', views.delete_chat, name='add_member'),
    path('delete_member/', views.delete_chat, name='delete_member'),
    path('edit/', views.edit_chat, name='edit_chat'),
    path('info/', views.get_info_chat, name='chat_info'),
    path('info_user/', views.get_user_chats, name='info_user'),
    path('messages_chat/', views.get_info_chat, name='chat_info'),
]