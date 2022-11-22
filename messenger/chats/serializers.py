from django.shortcuts import get_object_or_404
from rest_framework import serializers

from chats.models import Chat, Message
from users.models import User


class ChatListSerializer(serializers.ModelSerializer):
    members = serializers.ListField(source='get_members', required=False, read_only=True)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members'


class ChatSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                 many=True)
    messages = serializers.ListField(source='get_messages', read_only=True)

    class Meta:
        model = Chat
        fields = 'id', 'title', 'description', 'members', 'messages'


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Message
        fields = 'id', 'user', 'content', 'time_create', 'mark'


class ChatSendMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # chat = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = 'id', 'user', 'content', 'time_create', 'chat', 'mark'
