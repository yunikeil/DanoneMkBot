from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship, Mapped

from core.database import Base

if TYPE_CHECKING:
    from .shopping_cart import ShoppingCart


class UserRoleEnum(Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "user"

    tg_id = Column(Integer, primary_key=True)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    created_at = Column(Integer)
    
    shopping_carts: Mapped[list["ShoppingCart"]] = relationship(
        back_populates="user", lazy="selectin"
    )
    
    def is_admin(self):
        return self.role == UserRoleEnum.ADMIN

