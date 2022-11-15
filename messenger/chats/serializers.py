from rest_framework import serializers

from chats.models import Chat, Message
from users.models import User


class ChatListSerializer(serializers.ModelSerializer):
    members = serializers.ListField(source='get_members', required=False, read_only=True)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members'


class ChatSerializer(serializers.ModelSerializer):
    members = serializers.MultipleChoiceField(source='get_members',
                                              choices=[(choice.pk, choice.username) for choice in User.objects.all()])
    messages = serializers.ListField(source='get_messages', read_only=True)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members', 'messages'


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = 'id', 'user', 'content', 'time_create', 'mark'


class ChatSendMessageSerializer(serializers.ModelSerializer):
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all(),
                                                 many=False)

    def get_chat_id(self, message):
        print(message.chat.pk)
        return message.chat.pk

    class Meta:
        model = Message
        fields = 'id', 'user', 'content', 'time_create', 'chat', 'mark'
