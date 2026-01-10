# # shop/tasks.py
# from celery import shared_task
# from django.core.mail import send_mail
#
# @shared_task
# def send_email_task(subject, message, from_email, recipient_list):
#     send_mail(subject, message, from_email, recipient_list, fail_silently=False)
# shop/tasks.py
from celery import shared_task
from asgiref.sync import async_to_sync
from aiogram import Bot
from django.conf import settings

from .models import Orders


@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3, "countdown": 5})
def send_order_to_user(self, order_id):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    order = (
        Orders.objects
        .select_related("user")
        .prefetch_related("items__tea_item")
        .get(id=order_id)
    )

    lines = []
    total = 0
    currency = ""

    for item in order.items.all():
        line_total = item.price * item.quantity
        total += line_total
        currency = item.currency or currency

        lines.append(
            f" {item.tea_item.name} — {item.quantity} × {item.price} {item.currency}"
        )

    text = (
        "🧾 *Заказ оформлен*\n\n"
        + "\n".join(lines)
        + f"\n\n💰 Итого: {total} {currency}"
    )

    async_to_sync(bot.send_message)(
        chat_id=order.user.tg_id,
        text=text,
        parse_mode="Markdown"
    )
