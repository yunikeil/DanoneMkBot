from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from core.database import Base
from .user import User
from .catalog import Catalog


class ShoppingCart(Base):
    __tablename__ = "shopping_cart"

    catalog_id = Column(Integer, ForeignKey("catalog.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.tg_id"), primary_key=True)
    count = Column(Integer)

    catalog: Mapped["Catalog"] = relationship(lazy="selectin")
    user: Mapped["User"] = relationship(
        back_populates="shopping_carts", lazy="selectin"
    )
