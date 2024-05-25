from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    fullname = State()
    user_id = State()
    image = State()
    finish = State()
