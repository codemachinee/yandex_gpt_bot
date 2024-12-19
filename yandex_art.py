import asyncio

from PIL import Image
import io

from aiogram.types import BufferedInputFile

from paswords import*

from yandex_cloud_ml_sdk import YCloudML
from concurrent.futures import ThreadPoolExecutor

# Создаем фиксированный пул с 1 потоком
executor = ThreadPoolExecutor(max_workers=1)


async def run_in_executor(func, *args):
    """Используем фиксированный пул потоков для выполнения задач."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, func, *args)


async def save_image(image_bytes: bytes, output_path: str) -> None:
    """Сохраняет изображение из байтов."""
    with open(output_path, "wb") as f:
        f.write(image_bytes)
    print(f"Изображение сохранено в {output_path}")


async def display_image(image_bytes: bytes) -> None:
    """Открывает изображение из байтов."""
    image = Image.open(io.BytesIO(image_bytes))
    image.show()


async def send_image_to_telegram(bot, image_bytes, chat_id):
    # Создаем объект InputFile из байтов изображения
    image_file = BufferedInputFile(image_bytes, filename='image.jpeg')
    await bot.send_photo(chat_id, photo=image_file)
    print("Изображение отправлено в Telegram")


async def generate_images(description, width_value, height_value):
    sdk = YCloudML(folder_id=yandex_gpt_catalog_id, auth=yandex_gpt_api_key)
    model = sdk.models.image_generation('yandex-art')
    model = model.configure(width_ratio=int(width_value), height_ratio=int(height_value), seed=53)
    operation = await run_in_executor(model.run_deferred, description)
    result = await run_in_executor(operation.wait)
    # освобождаем ресурсы фиксированного пула потоков после выполнения завершения операции в потоке
    executor.shutdown(wait=True)
    return result.image_bytes
    # await save_image(result.image_bytes, "simple_image_async.jpeg")
