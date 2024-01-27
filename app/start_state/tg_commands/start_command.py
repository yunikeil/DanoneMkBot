from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


def get_start_command():
    names = ["start", "help"]
    
    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Привет! Это тестовая версия бота.")
    
    return CommandHandler(command=names, callback=command)


commands = [get_start_command()]
