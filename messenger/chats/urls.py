from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    # path('chat_page/<chat_id>', views.chat_page),
    path('create/', views.create_chat, name='create_chat'),
    path('delete/', views.delete_chat, name='delete_chat'),
    path('<chat_id>/edit/', views.edit_chat, name='edit_chat'),
    path('<chat_id>/info/', views.get_info_chat, name='chat_info'),
    path('<user_id>/', views.get_user_chats, name='user_chats')
]