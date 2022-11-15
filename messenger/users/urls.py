from django.urls import path

from .views import *

urlpatterns = [
    path('', UsersList.as_view(), name='users'),
    path('<int:pk>/', UserView.as_view(), name='user'),
    path('add_member/', add_member, name='add_member'),
    path('delete_member/', delete_member, name='delete_member'),
]


