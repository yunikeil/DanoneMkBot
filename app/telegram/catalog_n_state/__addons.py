from telegram import InlineKeyboardButton, InlineKeyboardMarkup










def generate_buttons(height: int = 1, length: int = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          -00):
    result: list[list[InlineKeyboardButton]] = []
    for l in range(length):
        result.append([])
        for h in range(height):
            result[l].append(InlineKeyboardButton(f"button:{l}", callback_data=f"call:{l}"))

    return result
    




catalog_text = "Вы в каталоге..."
catalog_keyboard = InlineKeyboardMarkup(generate_buttons())
