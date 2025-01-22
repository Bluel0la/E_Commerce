from sqlalchemy import Column, Integer, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from api.db.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    cart_item_id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey("carts.cart_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.item_id"), nullable=False)
    amount = Column(Integer, CheckConstraint("amount > 0"), nullable=False)
    price = Column(Float, CheckConstraint("price >= 0"), nullable=False)

    # Relationships
    cart = relationship("Cart", back_populates="cart_items")
    item = relationship("Item", back_populates="cart_items")
