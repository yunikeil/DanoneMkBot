from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from core.settings import config


def check_is_user_admin(tg_id: int):
    if tg_id in config.ADMIN_IDS:
        return True


admin_text = "Вы в админ-панельке, {user_name}"
admin_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Добавить товар", callback_data="create_catalog"),
        ],
        [
            InlineKeyboardButton("Удалить товаров", callback_data="delete_catalog"),
        ],
        [
            InlineKeyboardButton("Изменить товар", callback_data="update_catalog"),
        ],
        [
            InlineKeyboardButton("Закрыть меню", callback_data="close_admin"),
        ],

    ]
)
