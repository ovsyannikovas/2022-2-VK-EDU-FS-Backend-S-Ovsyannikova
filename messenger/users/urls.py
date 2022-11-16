from django.urls import path

from .views import *

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('<int:pk>/', UserView.as_view(), name='user'),
]
