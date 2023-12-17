import requests
prompt = {
    "modelUri": f"gpt://{yandex_gpt_catalog_id}/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.4,
        "maxTokens": "150"
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
            "text": f'В сатирической форме поздравь с днем рождения Алексея с учетом следующих фактов:'
                    f'1) Леха это стиль и харизма Востока. '
                    f'2) Леха любит когда все в этой жизни не дольше 4 минут. '
                    f'3) Леха любит все что горит и дымит. '
                    f'4) Новое хобби Алексея заключается в комментировании фильмов под пиво. '
                    f'5) Леха заботливо следит чтобы все напились как следует и очень расстраивается если кто то не пьет. '
                    f'6) Леха бывший успешный тиктокер и школьный диджей!'
        },

    ]
}

url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {yandex_gpt_api_key}"
}

response = requests.post(url, headers=headers, json=prompt)
answer = response.json()['result']['alternatives'][0]['message']['text']
print(answer)

# f'Ты Артур, бот который профессионально в сатирической форме, развернуто поздравляет с днем рождения'
#                     f'и обязательно с применением шуток на тему гомосексуальности виновника торжества'
