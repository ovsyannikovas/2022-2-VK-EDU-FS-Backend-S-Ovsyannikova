from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('chat_page/<name>', views.chat_page),
    path('create/', views.create_chat, name='create_chat'),
]