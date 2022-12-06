import json

import requests

from chats.models import Message
from datetime import datetime
from application.config import Config


def count_unmark_messages():
    user_messages = Message.objects.all()
    result = len(tuple(filter(lambda x: x.mark is False, user_messages)))
    date = str(datetime.now())
    return result, date


def write_logs(num, date):
    with open('logs.txt', 'a') as file:
        file.write(f'{date} - all_unmark_messages: {num}\n')


def publish_message(new_message, channel='chat'):
    command = {
        'method': 'publish',
        'params': {
            'channel': channel,
            'data': f'{new_message}'
        }
    }

    api_key = Config.API_KEY
    data = json.dumps(command)
    headers = {'Content-type': 'application/json', 'Authorization': 'apikey' + api_key}
    requests.post('http://localhost:8000/api', data=data, headers=headers)