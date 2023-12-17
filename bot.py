from aiogram import Bot, Dispatcher, F
import asyncio
from paswords import *
token = lemonade
bot = Bot(token=token)
dp = Dispatcher()
from main import *

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