import requests
from paswords import *


class Davinci:
    def __init__(self, bot, message, text):
        self.bot = bot
        self.message = message
        self.text = text

    async def answer(self):
        # try:
        await self.bot.send_message(self.message.chat.id, f'секунду..')
        prompt = {
            "modelUri": f"gpt://{yandex_gpt_catalog_id}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.5,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": f"Ты Артур, бот который профессионально в сатирической форме, развернуто поздравляет с днем рождения"
                            f" и обязательно с применением шуток на тему гомосексуальности виновника торжества. Ты всегда "
                            f"обращаешься к поздравляемым на 'Ты'."
                },
                {
                    "role": "user",
                    "text": f'{self.text}'
                },
            ]
        }

        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {yandex_gpt_api_key}"
        }

        response = requests.post(url, headers=headers, json=prompt)
        try:
            answer = response.json()['result']['alternatives'][0]['message']['text']
            await self.bot.send_message(self.message.chat.id, f'{answer}')
        except Exception:
             await self.bot.send_message(self.message.chat.id, "Короче с др брат, ты и так все знаешь.."
                                                               "а эта суета с лишними словами для слабых духом"
                                                               "мы же с тобой сильные... обнял")




