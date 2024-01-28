from .admin_command import admin_state_commands as __admin_state_commands
from .admin_states import admin_catalog_handler

admin_handlers = [
    *__admin_state_commands,
    admin_catalog_handler
]