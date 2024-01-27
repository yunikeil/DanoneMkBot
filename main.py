import asyncio

from telegram import Update
from telegram.ext import Application

from core.logger import setup_base_logger
from core.settings import config
from app.start_state import start_state_commands


async def init_application(application: Application) -> None:
    setup_base_logger("telegram")
    ...

if __name__ == "__main__":
    builder = Application.builder()
    builder.token(config.TG_TOKEN).post_init(init_application)
    
    application = builder.build()
    application.add_handlers(start_state_commands)
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)
