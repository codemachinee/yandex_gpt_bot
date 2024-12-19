from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from FSM import Form_image_generation
from yandex_art import generate_images, send_image_to_telegram


async def check_callbacks(callback: CallbackQuery, state: FSMContext):
    if callback.data.startswith('🎨'):
        await state.update_data(widht_hight=callback.data[1:].split(','))
    await callback.message.reply("Введите описание изображения которое хотите получить (Например: красный кот):")
    await callback.message.delete()
    await state.set_state(Form_image_generation.description)


async def description_registration(message: Message, bot, state: FSMContext):
    data = await state.get_data()
    data.get('name')
    await message.reply("Подождите идет генерация..")
    file = await generate_images(f'{message.text}', data.get('widht_hight')[0], data.get('widht_hight')[1])
    await send_image_to_telegram(bot, file, message.chat.id)
    await state.clear()