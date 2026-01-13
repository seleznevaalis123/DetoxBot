# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Orders
from django.conf import settings


@receiver(post_save, sender=Orders)
def notify_manager_on_order(sender, instance, created, **kwargs):
    if created:
        subject = f'Новый заказ #{instance.id}'
        message = f'Создан новый заказ. Детали:\n\n{instance}'
        manager_email = 'selezneva.test@yandex.ru'
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [manager_email],
            fail_silently=False,
        )
