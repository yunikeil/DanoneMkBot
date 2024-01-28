from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ContextTypes

from .__addons import check_is_user_admin, admin_text, admin_keyboard


def get_admin_command():
    names = ["admin"]

    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_id = update.message.from_user.id
        username = update.message.from_user.name

        if not check_is_user_admin(user_id):
            return

        await update.message.reply_text(
            text=admin_text.format(user_name=username), reply_markup=admin_keyboard
        )

    return CommandHandler(command=names, callback=command)


admin_state_commands = [get_admin_command()]
