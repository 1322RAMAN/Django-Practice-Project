from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email_task(username, email):
    send_mail(
        subject="Welcome to Our Platform",
        message=f"Hi {username}, welcome to our platform!",
        from_email="ramandhiman1322@gmail.com",
        recipient_list=[email],
        fail_silently=False,
    )
