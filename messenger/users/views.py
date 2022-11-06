import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from chats.models import Chat
from users.models import User


@require_GET
def show_users(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append({
            "id": user.pk,
            "username": user.username,
            "phone": user.phone,
        })
    return JsonResponse({"users": user_list})


@require_POST
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


@require_GET
def get_user_info(request):
    request_data = json.loads(request.body)
    user = User.objects.get(pk=request_data['id'])
    response = {
        "id": user.pk,
        "username": user.username,
        "phone": user.phone,
    }
    return JsonResponse(response)
