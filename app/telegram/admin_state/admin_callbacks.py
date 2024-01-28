from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes


# TODO finish writing admin states
def get_create_catalog_callback():
    pattern = '^create_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="create_catalog")
    
    return CallbackQueryHandler(callback, pattern)


def get_delete_catalog_callback():
    pattern = '^delete_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="delete_catalog")
    
    return CallbackQueryHandler(callback, pattern)


def get_update_catalog_callback():
    pattern = '^update_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="update_catalog")
    
    return CallbackQueryHandler(callback, pattern)


def get_close_admin_callback():
    pattern = '^close_admin$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="close_admin")
    
    return CallbackQueryHandler(callback, pattern)