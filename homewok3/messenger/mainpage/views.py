from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET


@require_GET
@csrf_exempt
def homepage(request):
    return render(request, "index.html", content_type="text/html")
