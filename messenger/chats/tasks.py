from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, ADMINS
from application.celery import app
from chats.utils import count_unmark_messages, write_logs


@app.task
def send_members_email(members_emails=None):
    send_mail(
        subject="New chat created",
        message="Hey, new chat created",
        from_email=EMAIL_HOST_USER,
        recipient_list=ADMINS
    )


@app.task
def count_unmark():
    res = count_unmark_messages()
    write_logs(*res)
