from aiogram.fsm.state import StatesGroup, State

class Form_image_generation(StatesGroup):
    widht_hight = State()  # Состояние для ввода email
    description = State()


