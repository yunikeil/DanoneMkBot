import re

from telegram import Update
from telegram.ext import filters, ConversationHandler, MessageHandler, ContextTypes

from core.database import get_session
from app.services import create_catalog


def get_create_catalog_message():
    pattern = filters.TEXT

    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        user_message = update.message.text
        results: list[str] = []
        
        if results := re.findall(r"\w+\n\w+\n[0-9]+", user_message):
            async with get_session() as db_session:
                for result in results:
                    result = result.split("\n")
                    await create_catalog(
                        db_session, result[0], result[1], int(result[2])
                    )

        await update.message.reply_text(f"added: {len(results)} result(s)")
        return ConversationHandler.END

    return MessageHandler(pattern, callback)
