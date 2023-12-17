import requests
from paswords import *

saved_messages_davinci = []


class Davinci:
    global saved_messages_davinci

    def __init__(self, bot, message, text):
        self.bot = bot
        self.message = message
        self.text = text

    async def answer(self):
        saved_messages_davinci.insert(len(saved_messages_davinci) + 1, {
                    "role": "user",
                    "text": f'{self.text}'})
        await self.bot.send_message(self.message.chat.id, f'секунду..')
        prompt = {
            "modelUri": f"gpt://{yandex_gpt_catalog_id}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.2,
                "maxTokens": "300"
            },
            "messages": []
        }
        prompt['messages'] = {
                    "role": "system",
                    "text": f"Ты Давинчи, бот помощник знающий ответы на все вопросы. Ты даешь краткий и лаконичный "
                    f"ответ на любые вопросы, а также способен найти запрашиваемое в интернете. Ты максимально "
                    f"вежлив и учтив."
                }, *saved_messages_davinci
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {yandex_gpt_api_key}"
        }
        response = requests.post(url, headers=headers, json=prompt)
        try:
            answer = response.json()['result']['alternatives'][0]['message']['text']
            await self.bot.send_message(self.message.chat.id, f'{answer}')
            saved_messages_davinci.insert(len(saved_messages_davinci) + 1, {
                "role": "assistant",
                "text": f'{str(answer)}'})
            if len(saved_messages_davinci) >= 8:
                del saved_messages_davinci[0:5]
        except Exception:
             await self.bot.send_message(self.message.chat.id, f"Траблы с мотивацией\n"
                                                               f"Логи:{response.json()}")
             del saved_messages_davinci[-1]




