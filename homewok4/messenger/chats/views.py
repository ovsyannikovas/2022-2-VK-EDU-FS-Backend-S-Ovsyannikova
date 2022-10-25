from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime
from django.shortcuts import render


@require_GET
def homepage(request):
    return render(request, "index.html", content_type="text/html")


@require_GET
def chat_list(request):
    chats = [
        {
            'id': 1,
            'name': 'Person1',
            'content': 'Hello World1'
        },
        {
            'id': 2,
            'name': 'Person2',
            'content': 'Hello World2'
        },
        {
            'id': 3,
            'name': 'Person3',
            'content': 'Hello World3'
        },
    ]
    return JsonResponse(chats, safe=False)


@require_POST
@csrf_exempt
def create_chat(request):
    chats = [{
        'id': 1,
        'name': 'Person1',
        'content': 'Hello World1'
    }, {
        'id': 2,
        'name': 'Person2',
        'content': 'Hello World2'
    }, {
        'id': 3,
        'name': 'Person3',
        'content': 'Hello World3'
    }, {
        'id': 4,
        'name': request.GET['name'],
        'content': request.GET['content']
    }]
    return JsonResponse(chats, safe=False)


@require_http_methods(['GET', 'POST'])
@csrf_exempt
def chat_page(request, name):
    messages = [{
        'id': 1,
        'name': 'Me',
        'content': 'Hello World',
        'date': '2022-10-11',
        'time': '9:46'
    }, {
        'id': 2,
        'name': name,
        'content': 'Hello Python',
        'date': '2022-10-11',
        'time': '9:50'
    }]
    if request.method == 'POST':
        messages.append({
            'id': 3,
            'name': 'Me',
            'content': request.GET['content'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M')
        })
    return HttpResponse(content=f"Страница чата {name}")
