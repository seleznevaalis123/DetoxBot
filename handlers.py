from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackQuery
from keyboards import get_main_blank, kb_announcements
from keyboards import MyCallback
from shop import users

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await users.cmd_start_db(message.from_user.id, message.from_user.username)
    await message.reply_photo(
        photo='https://www.turboimagehost.com/p/108138264/smd_start.jpg.html',
        caption='ДОБРО ПОЖАЛОВАТЬ В PANDA TEA BALI BOT!',
        reply_markup=get_main_blank())
    await message.delete()


@router.callback_query(MyCallback.filter(F.foo == 'back main'))
async def get_back_main(query: CallbackQuery, callback_data: MyCallback):
    await query.message.delete_reply_markup()
    await query.message.reply_photo(
        photo='https://www.turboimagehost.com/p/108138264/smd_start.jpg.html',
        caption='ДОБРО ПОЖАЛОВАТЬ В PANDA TEA BALI BOT!',
        reply_markup=get_main_blank())
    await query.message.delete()


@router.callback_query(MyCallback.filter(F.foo == 'announcement'))
async def get_announcement(query: CallbackQuery, callback_data: MyCallback):
    await query.message.delete_reply_markup()
    announcement_photo, caption = await users.get_announcements()
    await query.message.reply_photo(
        photo=announcement_photo,
        caption=caption,
        reply_markup=kb_announcements())
    await query.message.delete()

