from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

from .__addons import catalog_text, catalog_keyboard


def get_catalog_callback():
    pattern = '^catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        await query.answer()

        await query.edit_message_text(text=catalog_text, reply_markup=catalog_keyboard)
    
    return CallbackQueryHandler(callback, pattern)


catalog_callbacks = [get_catalog_callback()]
