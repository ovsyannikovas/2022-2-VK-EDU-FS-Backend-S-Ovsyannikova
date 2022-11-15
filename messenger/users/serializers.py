from rest_framework import serializers

from chats.models import Chat, Message
from users.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    chats = serializers.SerializerMethodField(source='get_chats')

    def get_chats(self, user):
        chats = Chat.objects.filter(members=user)
        chat_list = []
        for chat in chats:
            chat_list.append({
                "id": chat.pk,
                "title": str(chat.title),
            })
        return chat_list

    class Meta:
        model = User
        fields = 'id', 'username', 'phone', 'chats'


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username'
