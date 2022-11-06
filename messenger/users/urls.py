from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_users, name='show_users'),
    path('add_member', views.add_member, name='add_member'),
    path('delete_member', views.delete_member, name='delete_member'),
    path('info', views.get_user_info, name='user_info'),
]


