from aiogram import Bot, Dispatcher, F, types
import asyncio
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from FSM import Form_image_generation
from handlers import check_callbacks, description_registration
from paswords import *

token = lemonade
bot = Bot(token=token)
dp = Dispatcher()
from yandex_gpt import *


@dp.message(Command(commands='start'))
async def start(message, state: FSMContext):
    await state.clear()
    await bot.send_message(message.chat.id, text=f'/generate_image - генерация изображения')


@dp.message(Command(commands='generate_image'))
async def generate_image(message):
    but1 = types.InlineKeyboardButton(text='↔️1:2↕️', callback_data='🎨1,2')
    but2 = types.InlineKeyboardButton(text='↔️4:6↕️', callback_data='🎨4,6')
    but3 = types.InlineKeyboardButton(text='↔️2:2↕️', callback_data='🎨2,2')
    but4 = types.InlineKeyboardButton(text='↔️3:2↕️', callback_data='🎨3,2')
    but5 = types.InlineKeyboardButton(text='↔️6:4↕️', callback_data='🎨6,4')
    but6 = types.InlineKeyboardButton(text='↔️4:2↕️', callback_data='🎨4,2')
    kb2 = types.InlineKeyboardMarkup(inline_keyboard=[[but1], [but2], [but3], [but4], [but5], [but6]],
                                     resize_keyboard=False)
    await bot.send_message(message.chat.id, f'Выберите соотношение сторон генерируемого изображения:',
                           reply_markup=kb2)


dp.callback_query.register(check_callbacks, F.data)
dp.message.register(description_registration, Form_image_generation.description)


@dp.message(F.text)
async def chek_message(message):
    if 'Давинчи' in message.text:
        b = str(message.text).replace('Давинчи ', '', 1).replace('Давинчи, ',
                                      '', 1).replace('Давинчи,', '',
                                      1).replace(' Давинчи', '', 1)
        await Davinci(bot, message, b).answer()
    elif 'давинчи' in message.text:
        b = str(message.text).replace('давинчи ', '', 1).replace('давинчи, ',
                                      '', 1).replace('давинчи,', '',
                                      1).replace(' давинчи', '', 1)
        await Davinci(bot, message, b).answer()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')