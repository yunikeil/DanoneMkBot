from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ContextTypes

from .__addons import main_text, main_keyboard


def get_main_command():
    names = ["main"]

    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            text=main_text,
            reply_markup=main_keyboard,
        )

    return CommandHandler(command=names, callback=command)


main_commands = [get_main_command()]
