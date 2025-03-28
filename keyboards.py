from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import WebAppInfo


class MyCallback(CallbackData, prefix="my"):
    foo: str


def get_main_blank():
    builder = InlineKeyboardBuilder()
    miniapp_url = "https://5ktxzpmb-3000.uks1.devtunnels.ms/"
    builder.add(InlineKeyboardButton(text="㊙️МАГАЗИН",web_app=WebAppInfo(url=miniapp_url))),
    builder.add(InlineKeyboardButton(text='💗TG ДВИЖ', url='https://t.me/panda_tea_bali')),
    builder.add(InlineKeyboardButton(text='📣АНОНСЫ', callback_data=MyCallback(foo='announcement').pack())),
    builder.add(InlineKeyboardButton(text='📱INSTAGRAM', url='https://instagram.com/pandatea_bali')),
    return builder.adjust(2).as_markup()


def kb_announcements():
    builder1 = InlineKeyboardBuilder()
    builder1.add(InlineKeyboardButton(text='↩️ГЛАВНОЕ МЕНЮ', callback_data=MyCallback(foo='back main').pack()))
    return builder1.adjust(1).as_markup()
