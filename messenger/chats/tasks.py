from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER, ADMINS
from application.celery import app


@app.task
def send_admin_email():
    send_mail(
        subject="New chat created",
        message="Hey, new chat created",
        from_email=EMAIL_HOST_USER,
        recipient_list=ADMINS
    )
