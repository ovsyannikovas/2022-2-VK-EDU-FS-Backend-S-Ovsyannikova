from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView, get_object_or_404, ListAPIView

from users.models import User
from users.serializers import UserInfoSerializer, UsersListSerializer


class UserView(LoginRequiredMixin, RetrieveAPIView):
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()


class UsersList(ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()
