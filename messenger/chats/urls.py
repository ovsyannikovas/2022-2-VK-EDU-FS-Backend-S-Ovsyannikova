from django.urls import path

from .views import *

urlpatterns = [
    path('', ChatList.as_view(), name='chat_list'),
    path('<int:pk>/', ChatView.as_view(), name='chat'),
    path('message/<int:pk>/', MessageView.as_view(), name='message'),
    path('<int:pk>/messages/', ChatSendMessage.as_view(), name='send_message'),

    path('new/', new_message, name='new'),
    path('testchat/', homepage2, name='testchat')
]
