from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from chats.tasks import send_members_email

from chats.models import Chat, Message

from chats.serializers import ChatSerializer, ChatListSerializer, MessageSerializer, ChatSendMessageSerializer
from chats.utils import publish_message


def homepage(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


def new_message(request):
    # .delay()
    publish_message(request.GET.get('text'))
    return JsonResponse({})


def homepage2(request):
    return render(request, "index2.html")


class ChatList(LoginRequiredMixin, ListCreateAPIView):
    serializer_class = ChatListSerializer

    def post(self, request, *args, **kwargs):
        chat = self.create(request, *args, **kwargs)
        send_members_email.delay()
        return chat

    def get_queryset(self):
        user_id = self.request.user.id
        return Chat.objects.filter(members=user_id)


class ChatView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Chat.objects.filter(members=user_id)


class ChatSendMessage(LoginRequiredMixin, ListCreateAPIView):
    serializer_class = ChatSendMessageSerializer

    def get_queryset(self):
        chat = get_object_or_404(Chat, pk=self.kwargs['pk'])
        return Message.objects.filter(chat=chat)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['chat'] = self.kwargs['pk']
        return context

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user in get_object_or_404(Chat, id=pk).members.all():
            return self.list(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only member can read chat messages'}, status=403)

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user in get_object_or_404(Chat, id=pk).members.all():
            return self.create(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only member can send messages to chat'}, status=403)


class MessageView(LoginRequiredMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer

    # lookup_field = 'pk'
    # queryset = Message.objects.all()

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if request.user in get_object_or_404(Message, id=pk).chat.members.all():
            return self.retrieve(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only member can read chat messages'}, status=403)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if get_object_or_404(Message, id=pk).user == request.user:
            return self.update(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only owner of the message can edit message'}, status=403)

    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if get_object_or_404(Message, id=pk).user == request.user:
            return self.partial_update(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only owner of the message can edit message'}, status=403)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if get_object_or_404(Message, id=pk).user == request.user:
            return self.destroy(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Only owner of the message can delete message'}, status=403)
