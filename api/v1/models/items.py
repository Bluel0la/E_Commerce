from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from api.db.database import Base


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    item_name = Column(String(255), nullable=False)
    cost = Column(Float, CheckConstraint("cost >= 0"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    stock_amount = Column(Integer, default=0)

    # Relationships
    category = relationship("Category", back_populates="items")
    cart_items = relationship("CartItem", back_populates="item")
