from django.urls import path

from mainpage.views import homepage

urlpatterns = [
    path('', homepage, name="home")
]
