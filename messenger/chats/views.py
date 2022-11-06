import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime
from django.shortcuts import render

from chats.models import Chat, User, Message


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


def get_messages_json(messages):
    msg_list = []
    for message in messages:
        msg_list.append({
            "id": message.pk,
            "user": str(message.user),
            "content": message.content,
            "time create": message.time_create,
            "mark": message.mark
        })
    return msg_list


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


@require_http_methods('DELETE')
@csrf_exempt
def delete_chat(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    chat.delete()
    chats = Chat.objects.all()
    return JsonResponse(get_chats_json(chats))


@require_GET
def chat_info(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    return JsonResponse(get_chats_json((chat,)))


@require_GET
def get_user_chats(request, user_id):
    chats = Chat.objects.filter(author=User.objects.get(pk=user_id))
    return JsonResponse(get_chats_json(chats))


@require_POST
@csrf_exempt
def edit_chat(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    chat.title = request_data['title'] if 'title' in request_data else chat.title
    chat.description = request_data['description'] if 'description' in request_data else chat.description
    chat.save()
    response = {
        'id': chat.pk,
        'title': chat.title,
        'description': chat.description,
    }
    return JsonResponse(response)


@require_GET
def chat_messages(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    messages = Message.objects.filter(chat=chat)
    return JsonResponse({chat.title: get_messages_json(messages)})


@require_POST
@csrf_exempt
def mark_read(request):
    request_data = json.loads(request.body)
    message = Message.objects.get(pk=request_data['id'])
    message.mark = not message.mark
    message.save()
    return JsonResponse(get_messages_json((message,))[0])


@require_POST
@csrf_exempt
def send_message(request):
    request_data = json.loads(request.body)
    chat = Chat.objects.get(pk=request_data['id'])
    message = Message(
        chat=chat,
        content=request_data['content']
    )
    message.save()
    messages = Message.objects.filter(chat=chat)
    return JsonResponse({chat.title: get_messages_json(messages)})


@require_POST
@csrf_exempt
def edit_message(request):
    request_data = json.loads(request.body)
    message = Message.objects.get(pk=request_data['id'])
    message.content = request_data['content'] if 'content' in request_data else message.content
    message.save()
    return JsonResponse(get_messages_json((message,))[0])


@require_http_methods('DELETE')
@csrf_exempt
def delete_message(request):
    request_data = json.loads(request.body)
    message = Message.objects.get(pk=request_data['id'])
    message.delete()
    messages = Message.objects.all()
    return JsonResponse({"messages": get_messages_json(messages)})
