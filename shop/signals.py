from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Orders
import threading


@receiver(post_save, sender=Orders)
def notify_manager_on_order(sender, instance, created, **kwargs):
    if not created:
        return

    def send_email_safe():
        print("EMAIL SENDING STARTED")

        try:
            send_mail(
                subject=f"Новый заказ #{instance.id}",
                message=f"Создан новый заказ.\n\nЗаказ ID: {instance.id}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["selezneva.test@ya.ru"],
                fail_silently=False,
            )
            print("EMAIL SENT OK")

        except Exception as e:
            print("EMAIL ERROR:", repr(e))


    transaction.on_commit(
        lambda: threading.Thread(
            target=send_email_safe,
            daemon=True
        ).start()
    )
