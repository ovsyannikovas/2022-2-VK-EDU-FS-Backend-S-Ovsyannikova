import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime
from django.shortcuts import render

from chats.models import Chat, User


@require_GET
def homepage(request):
    return render(request, "index.html", content_type="text/html")


def get_chats_json(chats):
    chat_list = []
    for chat in chats:
        chat_list.append({
            'id': chat.id,
            'title': chat.title,
            'description': chat.description,
            'members': [member.username for member in chat.members.all()],
        })
    response = {'chats': chat_list}
    return response


@require_GET
def chat_list(request):
    chats = Chat.objects.all()
    return JsonResponse(get_chats_json(chats))


@require_POST
@csrf_exempt
def create_chat(request):
    request_data = json.loads(request.body)
    Chat.objects.create(
        title=request_data['title'],
        description=request_data['description'],
    )
    chats = Chat.objects.all()
    return JsonResponse(get_chats_json(chats))


# @require_DELETE
@csrf_exempt
def delete_chat(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    chat.delete()
    chats = Chat.objects.all()
    return JsonResponse(get_chats_json(chats))


@require_GET
def get_info_chat(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)
    response = {
        'id': chat.pk,
        'title': chat.title,
        'description': chat.description,
        'author': str(chat.author),
        'category': str(chat.category),
    }
    return JsonResponse(response)


@require_GET
def get_user_chats(request, user_id):
    chats = Chat.objects.filter(author=User.objects.get(pk=user_id))
    return JsonResponse(get_chats_json(chats))


@require_POST
@csrf_exempt
def edit_chat(request, chat_id):
    chat = Chat.objects.get(pk=chat_id)
    chat.title = request.GET['title'] if 'title' in request.GET else chat.title
    chat.description = request.GET['description'] if 'description' in request.GET else chat.description
    response = {
        'id': chat.pk,
        'title': chat.title,
        'description': chat.description,
        'author': str(chat.author),
        'category': str(chat.category),
    }
    return JsonResponse(response)


