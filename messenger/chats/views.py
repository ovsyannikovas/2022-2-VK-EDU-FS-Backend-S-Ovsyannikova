import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, \
    RetrieveUpdateAPIView

from chats.models import Chat, User, Message

from chats.serializers import ChatSerializer, ChatListSerializer, MessageSerializer, ChatSendMessageSerializer


@require_GET
def homepage(request):
    return render(request, "index.html", content_type="text/html")


class ChatList(ListCreateAPIView):
    serializer_class = ChatListSerializer
    queryset = Chat.objects.all()


class ChatView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer

    def get_object(self):
        return get_object_or_404(Chat, pk=self.kwargs['pk'])


class ChatSendMessage(ListCreateAPIView):
    serializer_class = ChatSendMessageSerializer

    def get_queryset(self):
        chat = get_object_or_404(Chat, pk=self.kwargs['pk'])
        return Message.objects.filter(chat=chat)


class MessageView(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs['pk'])
