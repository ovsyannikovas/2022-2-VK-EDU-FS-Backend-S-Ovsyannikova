from rest_framework.generics import RetrieveAPIView, get_object_or_404, ListAPIView

from users.models import User
from users.serializers import UserInfoSerializer, UsersListSerializer


class UserView(RetrieveAPIView):
    serializer_class = UserInfoSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()


class UsersList(ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()
