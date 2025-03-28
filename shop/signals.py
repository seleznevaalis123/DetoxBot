# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Orders
from shop.tasks import send_email_task


@receiver(post_save, sender=Orders)
def notify_new_order(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(
            'Новый заказ',
            f'Создан новый заказ с ID: {instance.id}',
            'selezneva.test@gmail.com',
            ['selezneva.test@gmail.com']
        )

