import threading
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Orders


@receiver(post_save, sender=Orders)
def notify_manager_on_order(sender, instance, created, **kwargs):
    if not created:
        return

    def send():
        send_mail(
            subject=f'Новый заказ #{instance.id}',
            message=f'Создан новый заказ.\n\n{instance}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['selezneva.test@ya.ru'],
            reply_to=["no-reply@ya.ru"],
            fail_silently=True,
        )

    transaction.on_commit(
        lambda: threading.Thread(target=send, daemon=True).start()
    )
