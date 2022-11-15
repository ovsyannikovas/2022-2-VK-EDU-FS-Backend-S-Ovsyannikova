from rest_framework import serializers

from chats.models import Chat, Message
from users.models import User


class ChatListSerializer(serializers.ModelSerializer):
    members = serializers.CharField(source='get_members', required=False)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members'


class ChatSerializer(serializers.ModelSerializer):
    members = serializers.ChoiceField(source='get_members', choices=User.objects.all())
    messages = serializers.ListField(source='get_messages', read_only=True)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members', 'messages'


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Message
        fields = 'id', 'user', 'content', 'time_create', 'mark'
