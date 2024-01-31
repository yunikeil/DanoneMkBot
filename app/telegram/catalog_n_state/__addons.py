from telegram import InlineKeyboardButton, InlineKeyboardMarkup


catalog_text = "Вы в каталоге..."


def get_offset_limit_buttons(current_offset: int, current_limit: int, catalog_count: int):
    previous_offset = max(0, current_offset - current_limit)
    next_offset = max(0, current_offset + current_limit)
            
    is_first_page = current_offset == 0
    is_last_page = current_offset + current_limit >= catalog_count
   
    return [
        [
            InlineKeyboardButton("⏪" if not is_first_page else "⏪❌", callback_data=f"catalog:{0}:{10}" if not is_first_page else f"catalog:-1:-1"),
            InlineKeyboardButton("◀️" if not is_first_page else "⬅️❌", callback_data=f"catalog:{previous_offset}:{current_limit}" if not is_first_page else f"catalog:-1:-1"),
            InlineKeyboardButton("▶️" if not is_last_page else "❌➡️", callback_data=f"catalog:{next_offset}:{current_limit}" if not is_last_page else f"catalog:-1:-1"),
            InlineKeyboardButton("⏩" if not is_last_page else "❌⏩", callback_data=f"catalog:{catalog_count - catalog_count % current_limit}:{current_limit}" if not is_last_page else f"catalog:-1:-1")
        ],
        [
            InlineKeyboardButton("Вернуться ↩️", callback_data=f"main")
        ]
    ]


def get_catalog_back_keyboard(catalog_id: int, current_offset: int, current_limit: int):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Быстрая покупка", callback_data=f"purchase:{catalog_id}")
            ],
            [
                InlineKeyboardButton("Добавить в корзину", callback_data=f"add_to_shopping_cart:{catalog_id}")
            ],
            [
                InlineKeyboardButton("Вернуться ↩️", callback_data=f"catalog:{current_offset}:{current_limit}")
            ]
        ]
    )




