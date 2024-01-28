from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes


def get_shopping_cart_callback():
    pattern = '^shopping_cart$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        await query.answer()

        await query.edit_message_text(text=f"Selected option: {query.data}")
    
    return CallbackQueryHandler(callback, pattern)


shopping_cart_callbacks = [get_shopping_cart_callback()]
