yandex_gpt_catalog_id = 1
text = 'Hi'
saved_messages_davinci = [{
                    "role": "user",
                    "text": f'Hello'}]
prompt = {
            "modelUri": f"gpt://{yandex_gpt_catalog_id}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.5,
                "maxTokens": "2000"
            },
            "messages": [

            ]
        }
saved_messages_davinci.insert(len(saved_messages_davinci) + 1, {
                    "role": "user",
                    "text": f'{text}'})

prompt['messages'] = {
                    "role": "system",
                    "text": f"Ты Артур, бот который профессионально в сатирической форме, развернуто поздравляет с днем рождения"
                            f" и обязательно с применением шуток на тему гомосексуальности виновника торжества. Ты всегда "
                            f"обращаешься к поздравляемым на 'Ты'."
                }, *saved_messages_davinci
print(prompt['messages'])