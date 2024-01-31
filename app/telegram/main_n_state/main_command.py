from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ContextTypes

from core.settings import config
from core.database import get_session
from app.services import get_user_by_tg_id
from .__addons import main_text, get_main_keyboard


def get_main_command():
    names = ["main"]

    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        async with get_session() as db_session:
            user = await get_user_by_tg_id(
                db_session, update.message.from_user.id
            )
        
        await update.message.reply_text(
            text=main_text,
            reply_markup=get_main_keyboard(update.callback_query.from_user.id in config.ADMIN_IDS),
        )

    return CommandHandler(command=names, callback=command)


main_commands = [get_main_command()]
