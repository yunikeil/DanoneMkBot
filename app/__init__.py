from .start_n_state import start_state_handlers
from .main_n_state import main_state_handlers

from .catalog_n_state import catalog_handlers
from .shopping_cart_n_state import shopping_cart_handlers
from .about_us_n_state import about_us_handlers
from .personal_cabinet_n_state import personal_cabinet_handlers


bot_handlers = [
    *start_state_handlers,
    *main_state_handlers,
    *catalog_handlers,
    *shopping_cart_handlers,
    *about_us_handlers,
    *personal_cabinet_handlers,
]
