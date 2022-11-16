from rest_framework.generics import RetrieveAPIView, get_object_or_404, ListAPIView

from users.models import User
from users.serializers import UserInfoSerializer, UsersListSerializer


class UserView(RetrieveAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])


class UsersList(ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()
