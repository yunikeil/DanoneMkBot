from telegram import InlineKeyboardButton, InlineKeyboardMarkup


main_text = "Добро пожаловать в главное меню бота! Выберите интересующий вас раздел"
main_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Каталог товаров", callback_data="catalog:0:10"),
        ],
        [
            InlineKeyboardButton(
                "Корзина товаров", callback_data="shopping_cart"
            ),
        ],
        [
            InlineKeyboardButton("О нас", callback_data="about_us"),
            InlineKeyboardButton(
                "Личный кабинет", callback_data="personal_cabinet"
            ),
        ],
    ]
)
