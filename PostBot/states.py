from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    fullname = State()
    user_id = State()
    image = State()
    finish = State()


class AdminAdvertisement(StatesGroup):
    photo = State()
    caption = State()
    inline_button_name = State()
    inline_button_url = State()
    finish = State()
