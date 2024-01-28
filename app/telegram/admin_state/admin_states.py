from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler

from .admin_callbacks import get_create_catalog_callback, get_delete_catalog_callback, get_update_catalog_callback, get_close_admin_callback
from .admin_message import get_create_catalog_message


admin_catalog_handler = ConversationHandler(
    entry_points=[get_create_catalog_callback(), get_delete_catalog_callback(), get_update_catalog_callback(), get_close_admin_callback()],
    states={
        "enter_new_catalogs_data": [get_create_catalog_message()],
    },
    fallbacks=[]
)

