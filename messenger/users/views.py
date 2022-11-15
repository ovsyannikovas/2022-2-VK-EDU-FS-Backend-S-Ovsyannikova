import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveAPIView, get_object_or_404, ListAPIView

from chats.models import Chat
from users.models import User
from users.serializers import UserInfoSerializer, UsersListSerializer


@require_http_methods('PUT')
@csrf_exempt
def add_member(request):
    request_data = json.loads(request.body)
    user = User.objects.get(pk=request_data['id'])
    chat = Chat.objects.get(pk=request_data['chat_id'])
    if user not in chat.members.all():
        chat.members.add(user)
    return JsonResponse({'chat_users': [mem.username for mem in chat.members.all()]})


@require_http_methods('DELETE')
@csrf_exempt
def delete_member(request):
    request_data = json.loads(request.body)
    user = User.objects.get(pk=request_data['id'])
    chat = Chat.objects.get(pk=request_data['chat_id'])
    if user in chat.members.all():
        chat.members.remove(user)
    return JsonResponse({'chat_users': [mem.username for mem in chat.members.all()]})


class UserView(RetrieveAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])


class UsersList(ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()

