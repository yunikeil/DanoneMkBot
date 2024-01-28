from inspect import cleandoc

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ContextTypes


def get_start_command():
    names = ["start", "help"]

    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(
            cleandoc(
                """
                Привет! Это тестовая версия бота.
                Для начала работы используйте /main.
                Тут возможно будет описание его возможностей.
                """
            )
        )

    return CommandHandler(command=names, callback=command)


start_state_commands = [get_start_command()]
