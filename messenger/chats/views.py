from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from chats.models import Chat, Message

from chats.serializers import ChatSerializer, ChatListSerializer, MessageSerializer, ChatSendMessageSerializer


@require_GET
@login_required
def homepage(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


class ChatList(ListCreateAPIView):
    serializer_class = ChatListSerializer
    queryset = Chat.objects.all()


class ChatView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer
    lookup_field = 'pk'
    queryset = Chat.objects.all()


class ChatSendMessage(ListCreateAPIView):
    serializer_class = ChatSendMessageSerializer

    def get_queryset(self):
        chat = get_object_or_404(Chat, pk=self.kwargs['pk'])
        return Message.objects.filter(chat=chat)


class MessageView(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    lookup_field = 'pk'
    queryset = Message.objects.all()
