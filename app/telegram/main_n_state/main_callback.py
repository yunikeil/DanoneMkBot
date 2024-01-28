from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from .__addons import main_text, main_keyboard


def get_main_callback():
    pattern = '^main$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text=main_text,
            reply_markup=main_keyboard,
        )
    
    return CallbackQueryHandler(callback, pattern)


main_callbacs = [get_main_callback()]
