from chats.models import Message
from datetime import datetime


def count_unmark_messages():
    user_messages = Message.objects.all()
    result = len(tuple(filter(lambda x: x.mark is False, user_messages)))
    date = str(datetime.now())
    return result, date


def write_logs(num, date):
    with open('logs.txt', 'a') as file:
        file.write(f'\n{date} - unmark_messages: {num}')
