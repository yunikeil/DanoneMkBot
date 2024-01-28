from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes


# TODO finish writing admin states
def get_create_catalog_callback():
    pattern = '^create_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="Введите по три строки каталоги")
        
        return "enter_new_catalogs_data"
    
    return CallbackQueryHandler(callback, pattern)


def get_delete_catalog_callback():
    pattern = '^delete_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="delete_catalog")
        
        return
    
    return CallbackQueryHandler(callback, pattern)


def get_update_catalog_callback():
    pattern = '^update_catalog$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="update_catalog")
        
        return
    
    return CallbackQueryHandler(callback, pattern)


def get_close_admin_callback():
    pattern = '^close_admin$'
    
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text="admin closed...")
    
    return CallbackQueryHandler(callback, pattern)

